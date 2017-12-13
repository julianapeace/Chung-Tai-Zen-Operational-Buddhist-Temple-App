$('document').ready(function(){
  console.log('this thingggyy')
});


$(document).ready(function () {
  console.log("it works")
  $('#section1').hide();
  $('#section2').hide();
  $('#section3').hide();
$('#section-header1').click(function(event){
  $('#section1').slideToggle()
  })
  $('#section-header2').click(function(event){
    $('#section2').slideToggle()
    })
    $('#section-header3').click(function(event){
      $('#section3').slideToggle()
      })
});
