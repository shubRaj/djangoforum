!function(e,n){"use strict";var o={settins:{bp:1024},dom:{$header:e(".js-header")},crnt:{init:function(){e(window).on("resize resizecurrent",function(){o.crnt.m=window.innerWidth<=o.settins.bp,o.crnt.d=!o.crnt.m}),e(window).trigger("resizecurrent")}},methods:{responsiveHandlers:function(n){e(window).on("resize.responsivehandlers responsivehandlers",function(){if(n.desktopBp!==o.crnt.d){n.desktopBp=o.crnt.d;var s=e(n.elem),t=n.namespace?"."+n.namespace:"";n.onDesktop===o.crnt.d?e.each(n.events,function(e,o){s.on(e+t,n.delegate,o)}):e.each(n.events,function(e){s.unbind(e+t)})}}),e(window).trigger("responsivehandlers")}},searchVisibleOnMobileBtn:function(){var e=o.dom.$header,n=o.dom.$header.find(".js-header-search-btn-open"),s=o.dom.$header.find(".js-header-search-btn-close");o.methods.responsiveHandlers({elem:n,namespace:"searchopen",onDesktop:!1,events:{click:function(){e.addClass("header--search")}}}),o.methods.responsiveHandlers({elem:s,namespace:"searchclose",onDesktop:!1,events:{click:function(){e.removeClass("header--search")}}})},dropdowns:function(){function n(e,n){if(!e.hasClass("js-dropdown-process")){e.addClass("js-dropdown-process");var o=e.hasClass("dropdown--open")?"slideUp":"slideDown";n=n||e.parents(".js-dropdown").find('[data-dropdown-btn="'+e.data("dropdown-btn")+'"]'),e.velocity(o,{complete:function(){e["slideUp"===o?"removeClass":"addClass"]("dropdown--open"),e.removeAttr("style").removeClass("js-dropdown-process")}}),n["slideUp"===o?"removeClass":"addClass"]("dropdown__btn--open")}}function o(o){var s=e("[data-dropdown-list].dropdown--open");if(o){var t=o.closest("[data-dropdown-list]");s=s.not(t)}n(s)}e(document).on("click",".js-dropdown [data-dropdown-btn]",function(s){var t=e(this),d=t.data("dropdown-btn"),r=t.parents(".js-dropdown").find('[data-dropdown-list="'+d+'"]');return o(r),n(r,t),s.preventDefault(),!1}),e(document).on("click",function(n){o(e(n.target))})},init:function(){for(var e in this)delete this.init,"function"==typeof this[e]?this[e]():this[e].init&&"function"==typeof this[e].init&&this[e].init();return this}};window.app=o.init()}(jQuery);