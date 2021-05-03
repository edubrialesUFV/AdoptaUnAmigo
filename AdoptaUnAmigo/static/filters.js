var currentdate = new Date();
$(document).ready(function () {
  $(".filter-1").click(function (e) {
      //console.log(e.target.value)

    if (e.target.value!='Subido hace') {
      
      $(".filter-1").addClass('exp')
      
    }
    else {
      $(".filter-1").removeClass('exp')
      
    }
});
});

$(document).ready(function () {
  $(".filter-2").click(function (e) {
      console.log(e.target.value)

    if (e.target.value!='Ciudad') {
      
      $(".filter-2").addClass('exp')
     
    }
    else {
      $(".filter-2").removeClass('exp')
      
    }
});
});