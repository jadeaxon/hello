// Services
// This will provide data shared between the scopes of the different subpages (views).
// This service gets injected into our controllers.
// Whenever you hit the browser refresh button, the service reinitializes its state.
// Simply navigating to different app subpages (#/foo URLs) should preserve state since that's all
// client-side navigation/routing.
//
// Our services collectively provide an API for accessing our overall system model.  Each service
// might help us access a particular class of objects, like cities.
// These client-side services might then call server-side services to read/write to a database so
// we get session, account, and system persistence.
//
// Daily forecast URL: http://api.openweathermap.org/data/2.5/forecast/daily?APPID=d48a9c26f43f66550ea09daea8feae43
// http://api.openweathermap.org/data/2.5/forecast/daily?q={city name},{country code}&cnt={cnt}
// http://api.openweathermap.org/data/2.5/forecast/daily?q=Provo,us&cnt=7&APPID=d48a9c26f43f66550ea09daea8feae43
// The daily stuff is now paid access only.  We can get current weather using this on the free
// account:
// http://api.openweathermap.org/data/2.5/weather?q=Provo,us&APPID=d48a9c26f43f66550ea09daea8feae43
// The API docs are here: https://openweathermap.org/current
weatherApp.service('cityService', function () {
	this.city = "Provo";

});

