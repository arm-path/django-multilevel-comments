from django.shortcuts import redirect
from django.db.models import Count
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormMixin
from django.contrib.auth.models import User

from comment.models import BlogComment
from comment.forms import BlogCommentForm
from .models import Blog


class PrimaryPageBlog(ListView):
    """ Blog list view """
    """ Представление списка блогов """
    model = Blog
    template_name = 'blog/primary.html'

    def get_context_data(self, **kwargs):
        """ Adding additional context to the blog view """
        """ Добавление дополнительного контекста к представлению списка блогов """
        context = super().get_context_data(**kwargs)
        context['title'] = 'Блог'
        return context

    def get_queryset(self):
        return Blog.objects.filter(posted_by=True)


class PageBlog(FormMixin, DetailView):
    """ Blog Submission """
    """ Представление блога """
    model = Blog
    form_class = BlogCommentForm
    initial = {}
    template_name = 'blog/blog.html'
    context_object_name = 'object'

    def post(self, request, *args, **kwargs):
        """ Receiving data sent by POST request. Form data comment """
        """ Получение данных отправленных POST запросом. Данные формы комментарий """
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        """ Checks the form, fills in the data, saves to the model """
        """ Проверяет форму, заполняет данные, сохраняет в модели """
        self.object = form.save(commit=False)
        self.object.blog = self.get_object()
        self.object.name = self.request.user
        self.object.save()
        return super().form_valid(form)

    def get_success_url(self):
        """ Redirects to the address on successful form validation. Comment forms """
        """ Перенаправляет по адресу, при успешном прохождении валидации формы. Формы комментарии """
        return reverse_lazy('blog_page', kwargs={'slug': self.kwargs['slug']})

    def get_context_data(self, **kwargs):
        """ Adding additional context to the blog view """
        """ Добавление дополнительного контекста к представлению блога """
        context = super().get_context_data(**kwargs)
        context['title'] = Blog.objects.get(slug=self.kwargs['slug'])
        context['comments'] = BlogComment.objects.annotate(
            cnt=Count('children')).filter(blog__slug=self.kwargs['slug'])
        return context


def сhange_model_comment(request, slug):
    """ Comments on articles, handling of links 'I like' and 'I don't like' """
    """ Комментарии к статьям, обработка ссылки 'мне нравиться' и 'мне не нравиться' """

    # 1.  Getting data from a post request, from hidden fields
    # 1. (Получение  данных из пост запроса, из скрытых полей)
    get_user = request.POST.get('get_user')
    get_obj_comment = request.POST.get('get_likes_or_dislikes')
    get_comment = BlogComment.objects.get(pk=request.POST.get('get_comment'))

    get_obj_user = User.objects.get(username=get_user)

    # 2.  Get a boolean value, about the content of the user among those who have checked 'I like' or 'I do not like'
    # 2. (Получение булевого значения, о содержании пользователя среди поставивших отметку 'мне нравиться' или 'мне не нравиться')
    exists_user_like = get_comment.like_user.filter(username=get_user).exists()
    exists_user_dislike = get_comment.dislike_user.filter(
        username=get_user).exists()

    # 3.  Checks button press I like
    # 3. (Проверяет нажатие кнопки мне нравиться)
    if get_obj_comment == 'likes':
        # 3.1  Checks user content among those who have checked I like
        # 3.1 (Проверяет содержание пользователя среди поставивших отметку мне нравиться)
        if exists_user_like:
            get_comment.like_user.remove(get_obj_user.pk)
            like = get_comment.like - 1
            get_comment.like = like
            get_comment.save()
        else:
            get_comment.like_user.add(get_obj_user)
            like = get_comment.like + 1
            get_comment.like = like
            get_comment.save()
            # 3.2  Before putting the mark 'I like', it checks the user's content among those who marked the mark I do not like, and removes it from this list
            # 3.2 (Перед проставлением отметки 'Мне нравиться', проверяет содержание пользователя среди поставивших отметку мне не нравиться, и удаляет из данного списка)
            if exists_user_dislike:
                get_comment.dislike_user.remove(get_obj_user.pk)
                dislike = get_comment.dislike - 1
                get_comment.dislike = dislike
                get_comment.save()
    # 4.  Checks button press I don't like
    # 4. (Проверяет нажатие кнопки мне не нравиться)
    elif get_obj_comment == 'dislikes':
        # 4.1  Checks the user's content among those who ticked I don't like
        # 4.1 (Проверяет содержание пользователя среди поставивших отметку мне не нравиться)
        if exists_user_dislike:
            get_comment.dislike_user.remove(get_obj_user.pk)
            dislike = get_comment.dislike - 1
            get_comment.dislike = dislike
            get_comment.save()
        else:
            get_comment.dislike_user.add(get_obj_user)
            dislike = get_comment.dislike + 1
            get_comment.dislike = dislike
            get_comment.save()
            # 4.2  Before checking the checkbox 'I do not like it', it checks the user's content among those who checked the checkbox I like, and removes it from this list
            # 4.2 (Перед проставлением отметки 'Мне не нравиться', проверяет содержание пользователя среди поставивших отметку мне нравиться, и удаляет из данного списка)
            if exists_user_like:
                get_comment.like_user.remove(get_obj_user.pk)
                like = get_comment.like - 1
                get_comment.like = like
                get_comment.save()
    return redirect('blog_page', slug=slug)
