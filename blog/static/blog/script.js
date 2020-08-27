let $containerLinksEvent = document.querySelector(".container-comments");
let $jsClassChangeDisplayNone = document.querySelectorAll(".jsClassChange");
let $jsNewPlaceholder = document.querySelectorAll(".jsPlaceholder .form-control");


//  Changes the placeholder in the response comments 
// (Измененяет placeholder в ответных комментариях)
changePlacehodler($jsNewPlaceholder);
function changePlacehodler(jsPlaceholder) {
  for (var i = 0; i < jsPlaceholder.length; i++) {
    jsPlaceholder[i].setAttribute("placeholder", "Ваш ответ");
  }
}

//  Cleans up comment response forms
// (Очищает формы ответных комментарий)
function clearCodeJS(jsSetFormDisplayNone) {
  for (var i = 0; i < jsSetFormDisplayNone.length; i++) {
    if (!jsSetFormDisplayNone[i].classList.contains("display-none")) {
      jsSetFormDisplayNone[i].classList.add("display-none");
    }
  }
}

//  Hides reveals the reply form to comments when clicking on the "Reply" link 
// (Скрывает раскрывает форму ответа к комментариям при щелчке по ссылке "Ответить")
$containerLinksEvent.addEventListener("click", function (event) {
  if (event.target.dataset.box) {
    var $jsClassChange = event.target.querySelector(".jsClassChange");
    if ($jsClassChange.classList.contains("display-none")) {
      clearCodeJS($jsClassChangeDisplayNone);
      $jsClassChange.classList.remove("display-none");
      event.target.classList.remove("answer")
    } else {
      $jsClassChange.classList.add("display-none");
      event.target.classList.add("answer")
    }
  }
  //  Hides reveals replies to comments when clicking on the "Answers" link
  // (Скрывает раскрывает ответы к комментариям при щелчке по ссылке "Ответы")
  if (event.target.dataset.square) {
    var $children = event.target.querySelector(".children");
    if ($children.classList.contains("display-none")) {
      $children.classList.remove("display-none");
      event.target.classList.remove("answer")
    } else {
      $children.classList.add("display-none");
      event.target.classList.add("answer")
    }
  }
  //  Specifies the user to whom you want to reply. Sends the result to a hidden input field for transmission to the server
  // (Определяет пользователя, к которому необходимо ответить. Передает результат в скрытое поле для ввода, для передачи на сервер)
  if (event.target.classList.contains("jsAnswerUser")) {
    event.target.addEventListener("click", function () {
      var $input = event.target.querySelector(".form-control");
      var $button = event.target.querySelector(".jsResponseToUser");
      var $userName = event.target.querySelector(".jsNameUser");
      $button.addEventListener("click", function () {
        if ($input.value != "") {
          console.log($userName.value);
          $input.value = $userName.value + ", " + $input.value;
          console.log($input.value);
        }
      });
    });
  }
});


// =======> Shows hide comments (Показывает скрывет комментарии)

let $getLiComment = document.querySelectorAll('.JSCountComment')
let $btnExpandСomment = document.querySelector('.JSexpandСomment')
let openComments = 3 // Number of comments per page (Количество комментарий на странице)


//  Displays the first 3(openComments) comments
// (Выводит первые 3(openComments) комментарий)
if ($getLiComment.length>openComments){
  for (let comment=openComments; comment < $getLiComment.length; comment ++){
    $getLiComment[comment].classList.add('display-none')
  }
}else{
  $btnExpandСomment.classList.add('display-none')
}

//  Shows the following comments on the page
// (Показывает следующие комментарии на странице)
$btnExpandСomment.addEventListener('click', ()=>{
  openComments += 3 
  for (let comment=0; comment < openComments; comment ++){
    if ($getLiComment[comment]){
      if ($getLiComment[comment].classList.contains('display-none')){
        $getLiComment[comment].classList.remove('display-none')
      }
    }else{
      $btnExpandСomment.classList.add('display-none')
    }
  }
})

