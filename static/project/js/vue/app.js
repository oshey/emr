var app = new Vue({

     el: '#app' ,

     mounted: function(){
        axios.defaults.headers.common['X-CSRFToken'] = this.getCookie('csrftoken');
     },

     methods: {
        getCookie: function(name) {
			var cookieValue = null;
			if (document.cookie && document.cookie !== '') {
				var cookies = document.cookie.split(';');
				for (var i = 0; i < cookies.length; i++) {
					var cookie = jQuery.trim(cookies[i]);
					// Does this cookie string begin with the name we want?
					if (cookie.substring(0, name.length + 1) === (name + '=')) {
						cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
						break;
					}
				}
			}

			return cookieValue;
		}
	}
});

axios.defaults.headers.common['xsrfCookieName'] = 'csrftoken';
axios.defaults.headers.common['xsrfHeaderName'] = 'X-CSRFToken';