window.onload = function () {
  "use strict";
  //pop-up start
  const popupLinks = document.querySelectorAll('.js-popup--link');
  const body = document.querySelector('body');
  const lockPadding = document.querySelectorAll('.lock--padding');

  let unlock = true;

  const timeOut = 500;

  if (popupLinks.length > 0) {
    for (let index = 0; index < popupLinks.length; index++) {
      const popupLink = popupLinks[index];
      popupLink.addEventListener("click", function (e) {
        const popupName = popupLink.getAttribute('href').replace('#', '');
        const curentPopup = document.getElementById(popupName);
        popupOpen(curentPopup);
        e.preventDefault();
      });
    }
  }

  const popupCloseIcon = document.querySelectorAll('.popup--close');
  if (popupCloseIcon.length > 0) {
    for (let index = 0; index < popupCloseIcon.length; index++) {
      const el = popupCloseIcon[index];
      el.addEventListener('click', function (e) {
        popupClose(el.closest('.popup'));
        e.preventDefault();
      });
    }
  }

  function popupOpen(curentPopup) {
    if (curentPopup && unlock) {
      const popupActive = document.querySelector('.popup.open');
      if (popupActive) {
        popupClose(popupActive, false);
      } else {
        bodyLock();
      }
      curentPopup.classList.add('open');
      curentPopup.addEventListener("click", function (e) {
        if (!e.target.closest('.popup__content')) {
          popupClose(e.target.closest('.popup'));
        }
      });
    }
  }

  function popupClose(popupActive, doUnlock) {
    if (unlock) {
      popupActive.classList.remove('open');
      if (doUnlock === undefined) {
        bodyUnLock();
      }
    }
  }

  function bodyLock() {
    const lockPaddingValue = window.innerWidth - document.querySelector('.body').offsetWidth + 'px';

    if (lockPadding.length > 0) {
      for (let index = 0; index < lockPadding.length; index++) {
        const el = lockPadding[index];
        el.style.paddingRight = lockPaddingValue;
      }
    }

    body.style.paddingRight = lockPaddingValue;
    body.classList.add('_fixed');
    unlock = false;
    setTimeout(function () {
      unlock = true;
    }, timeOut);
  }

  function bodyUnLock() {
    setTimeout(function () {
      if (lockPadding.length > 0) {
        for (let index = 0; index < lockPadding.length; index++) {
          const el = lockPadding[index];
          el.style.paddingRight = '0px';
        }
      }
      body.style.paddingRight = '0px';
      body.classList.remove('_fixed');
    }, timeOut);

    unlock = false;
    setTimeout(function () {
      unlock = true;
    }, timeOut);
  }
  document.addEventListener('keydown', function (e) {
    if (e.which === 27) {
      const popupActive = document.querySelectorAll('.popup.open');
      popupClose(popupActive);
    }
  });
  //pop-up end
};


$(function () {


  let width = $(window).width();
  let body = $('.body');

  $('.js-news-slider').slick({
    infinite: true,
    slidesToShow: 3,
    slidesToScroll: 1,
    responsive: [{
        breakpoint: 769,
        settings: {
          slidesToShow: 2
        }
      },
      {
        breakpoint: 577,
        settings: {
          slidesToShow: 1
        }
      },

    ]


  });


  $(document).on('click', '.js-close-option', function (e) {
    $('.table__sublist').slideUp();
  })

  $(document).on('click', '.js-table-option', function (e) {
    if ( $(this).parent().hasClass('_open')){
      $(this).parent().children('.table__sublist').slideUp();
      $(this).parent().removeClass('_open');
    } else {
      $('.table__sublist').slideUp();
      $(this).parent().children('.table__sublist').slideDown();
      $(this).parent().addClass('_open');
    }

  });

  $(document).on('click', '.js-table-btn', function (e) {
    e.preventDefault(e);
    $('.js-table-btn').removeClass('_active');
    $(this).addClass('_active');
  });

  $(document).on('click', '.js-toggle-balance', function (e) {
    e.preventDefault(e);
    $(this).toggleClass('_active');
    $('.balance__bottom').slideToggle();
  });
  


  $(document).on('click', '.js-menu-toggle', function (e) {
    e.preventDefault(e);
    $('.menu').toggleClass('_open');
    body.toggleClass('_fixed')
  });
});