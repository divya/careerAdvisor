$(document).ready(function() {

  function showModal(){
    $('.ui.modal').innerHTML = this.id;
    $('.ui.modal').modal('show');
  };

  $('.title').on('click',function(){ //bind click handler
    debugger;
    $('#thismodal').html("<h2>Description</h2><br>" +
      this.id);
    $('.ui.modal').modal('show');      //things to do on click
  })

});
