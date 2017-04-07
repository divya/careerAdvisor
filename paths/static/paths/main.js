$(document).ready(function() {

  function showModal(){
    $('.ui.modal').innerHTML = this.id;
    $('.ui.modal').modal('show');
  };

  // $('.title').on('click',function(){ //bind click handler
  //   $('#thismodal').html("<h2>Description</h2><br>" +
  //     this.id);
  //   $('.ui.modal').modal('show');      //things to do on click
  // })

});

function showDescription(desc, title){
  debugger;
  $('#thismodal').html("<h2>" + title + "</h2><br>" +
    desc);
  $('.ui.modal').modal('show');      //things to do on click
};

function togglePrevious(id){
  var steps = document.getElementsByClassName("before " + id);
  var shownSteps = document.getElementsByClassName("before " + id + " show")
  if(shownSteps.length > 0){
    var n = shownSteps.length
    for(var i=0; i<n; i++) {
      steps[i].className = "step before " + id;
    }
    beforeIcon = document.getElementById(id + "-before-icon");
    beforeIcon.className = "add circle icon";
  }
  else{
    var n = steps.length
    for(var i=0; i<n; i++) {
      steps[i].className = "step before " + id + " show";
    }
    beforeIcon = document.getElementById(id + "-before-icon");
    beforeIcon.className = "minus circle icon";
  }
};

function toggleAfter(id){
  var steps = document.getElementsByClassName("after " + id);
  var shownSteps = document.getElementsByClassName("after " + id + " show")
  if(shownSteps.length > 0){
    var n = shownSteps.length
    for(var i=0; i<n; i++) {
      steps[i].className = "step after " + id;
    }
    beforeIcon = document.getElementById(id + "-after-icon");
    beforeIcon.className = "add circle icon";
  }
  else{
    var n = steps.length
    for(var i=0; i<n; i++) {
      steps[i].className = "step after " + id + " show";
    }
    beforeIcon = document.getElementById(id + "-after-icon");
    beforeIcon.className = "minus circle icon";
  }
};
