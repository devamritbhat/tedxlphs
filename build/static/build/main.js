let seat_nos = [];  
let amt = 0;

function book_seat(){
  $("#Qty").removeAttr('disabled');
  $("#id_seats").val(seat_nos);
  sessionStorage.setItem("fade", "on");
  document.getElementById("tedx_form").submit();
}

function scrollError(){
  $([document.documentElement, document.body]).animate({
    scrollTop: $("#error").offset().top
}, 100);
}

$(document).ready(function(){
  $("body").addClass("overflow-hidden");
  if (sessionStorage.getItem("fade") == "on"){
    $('#greet').remove();     
  }
  else {
    $('#greet').fadeTo(500, 1)
    $('#greet').fadeTo(500, 0, "swing", function(){
      $('#greet').remove();     
    })
  }

  if (sessionStorage.getItem("fade") == "on"){
    $('.fadeto').delay(0).fadeTo(0, 1, function(){
      $("body").removeClass("overflow-hidden");
    });
    $('.fadeto2').delay(0).fadeTo(0, 1, function(){
      $("body").removeClass("overflow-hidden");
    });
    sessionStorage.setItem("fade", "off");
  }
  else {
      $('.fadeto').delay(900).fadeTo(1000, 1, function(){
        $("body").removeClass("overflow-hidden");
      });
      $('.fadeto2').delay(1500).fadeTo(1000, 1, function(){
        $("body").removeClass("overflow-hidden");
      });
  }

  $("#s-mb > div > div > button").addClass("rounded btn btn-sm btn-outline-light m-1 shadow-none").attr('type', 'button')
  $("#id_venue").addClass("form-select")
  $('#A > div > button, #B > div > button, #C > div > button, #D > div > button, #J > div > button').addClass('btn-secondary').removeClass('btn-outline-light').attr('disabled', 'disabled')
  $("#id_file").addClass("form-control").attr('id', 'formFile')
  if ($(window).width() < 768){
    $("#s-mb > .row").css("width", "350%")
    $(".modal-footer > .row").css("width", "350%")
    $(".categ").css("width", "350%")
  }

  $('#formFile, #trId').bind('keydown change', function() {
    var empty = false;
    $('#formFile, #trId').each(function() {
        if ($(this).val() == '') {
            empty = true;
        }
    });
    if (empty) 
    {
      $('#fin_btn').attr('disabled', 'disabled'); 
    } 
    else 
    {
      $('#fin_btn').removeAttr('disabled');
    }
  });

  $('#FirstName, #LastName, #Contact, #Email, #Age, #Qty').bind('keydown change', function() {
    var empty = false;
    $('#FirstName, #LastName, #Contact, #Email, #Age, #Qty').each(function() {
        if ($(this).val() == '') {
            empty = true;
        }
    });
    if (empty) 
    {
      $('#pos').attr('disabled', 'disabled'); 
    } 
    else 
    {
      $('#pos').removeAttr('disabled');
    }
  });

  
  $("#s-mb > div > div > button").click(function(){
    if ($("#s-mb > div > div .btn-light").length < $("#Qty").val() && $(this).hasClass("btn-outline-light")){
      $(this).toggleClass("btn-outline-light btn-light")
      seat_nos.push($(this).parent().parent().attr('id') + $(this).text())
      if ("ABCDEFGHIJ".indexOf($(this).parent().parent().attr('id')) >= 0){
        amt += 800
      }
      else {
        amt += 500
      }
    }
    else if ($(this).hasClass("btn-light")){
      $("#s-mb > div > div .btn-outline-light").toggleClass("pe-none")
      $(this).toggleClass("btn-outline-light btn-light")
      seat_nos.pop($(this).parent().parent().attr('id') + $(this).text())
      if ("ABCDEFGHIJ".indexOf($(this).parent().parent().attr('id')) >= 0){
        amt -= 800
      }
      else {
        amt -= 500
      }
    }

    if ($("#s-mb > div > div .btn-light").length == $("#Qty").val() && $("#Qty").val() > 0){
      $('#pro').removeAttr('disabled');
      $("#s-mb > div > div .btn-outline-light").addClass("pe-none");
    }
    else if ($("#s-mb > div > div .btn-light").length < $("#Qty").val() && $("#Qty").val() > 0)
    {
      $('#pro').attr('disabled', 'disabled');
      $("#s-mb > div > div .btn-outline-light").removeClass("pe-none");
    }

    $("#fin_btn").text("Book Tickets Worth Rs. " + amt)
  });

  $("#pos").click(function(){
    seat_nos = []; 
    amt = 0; 
    $('#pro').attr('disabled', 'disabled');
    $("#fin_btn").text("")
    $(".btn-light").toggleClass("btn-outline-light btn-light")
    $("#s-mb > div > div .btn-outline-light").removeClass("pe-none");
    if (!($("#Contact").val().match(/^\d{10}$/))){
      $("#error > div > div").text("Enter a valid 10-digit number. ")
      $("#error").removeClass('d-none')
      if ($(window).width() < 768){
        scrollError();
      }
    }

    else if (!($("#Email").val().match(/^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/))){
      $("#error > div > div").text("Enter a valid email address. ")
      $("#error").removeClass('d-none')
      if ($(window).width() < 768){
        scrollError();
      }
    }

    else if ($("#Qty").val() < 1){
      $("#error > div > div").text("Quantity must be greater than 0. ")
      $("#error").removeClass('d-none')
      if ($(window).width() < 768){
        scrollError();
      }
    }
    else {
      $("#error").addClass('d-none')
      $('#modal-seats').modal('show');
    }
  })
});


window.onscroll = function() {
  var winScroll = document.body.scrollTop || document.documentElement.scrollTop;
  var height = document.documentElement.scrollHeight - document.documentElement.clientHeight;
  var scrolled = (winScroll / height) * 100;
  if (scrolled > 99.48) scrolled = 100;
}

const observer = new IntersectionObserver((entries) => {
  entries.forEach((entry) => {
    if (entry.isIntersecting){
        if (entry.target.classList.contains("typewriter")){
          typeWriter();
        } else {
            entry.target.classList.add('show');
        }
    } else {
        entry.target.classList.remove('show');
    }
  });
});

const hiddenElements = document.querySelectorAll('.hidden');
hiddenElements.forEach((el) => observer.observe(el));

var i = 0;
var txt = 'Made with ❤️ by Team TEDxLPHS';

function typeWriter() {
  if (i < txt.length) {
    document.querySelector(".typewriter > span").innerHTML += txt.charAt(i);
    i++;
    setTimeout(typeWriter, 75);
  }
}
