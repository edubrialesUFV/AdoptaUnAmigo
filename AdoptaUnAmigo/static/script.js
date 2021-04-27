

$(document).ready(function () {
  function colorear(id) {
    storage = localStorage.getItem(id)
    console.log(storage)
    if (storage) {
      if (storage == 'rojo') {
        $('#' + id + ' > svg > .'+id).addClass('active');
      }
    }
  }

  
  const anuncios = document.querySelectorAll(".favorito");
  for (let anun of anuncios) {
    anun.value = anun.id;
    colorear(anun.id)
  }
});
function set_value() {
  const anuncios = document.querySelectorAll(".favorito");
  for (let anun of anuncios) {
    anun.value = anun.id;
  }
}
set_value();

$(document).ready(function () {
  $(".favorito").click(function () {
    id = '#'
    id = id + $(this).val();
    clas = '.'
    clas = clas + $(this).val();
    todo = id + '>' + 'svg' + '>' + clas

    key = $(this).val()
    
    if ($(todo).hasClass('active')) {
      $(todo).removeClass('active')
      localStorage.setItem(key, 'gris')
    }
    else {
      $(todo).addClass('active')
      localStorage.setItem(key, 'rojo')
    }

    //console.log($(this));

    $.ajax({
      url: '',
      type: 'get',
      data: {
        id_anunciofav: $(this).val()
      },

      success: function (response) {
        $(".favorito").val(response.id_anunciofav)
        set_value()
      }
    });
  });
});



