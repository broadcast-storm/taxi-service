(function(e){function t(t){for(var r,a,u=t[0],i=t[1],s=t[2],f=0,d=[];f<u.length;f++)a=u[f],Object.prototype.hasOwnProperty.call(o,a)&&o[a]&&d.push(o[a][0]),o[a]=0;for(r in i)Object.prototype.hasOwnProperty.call(i,r)&&(e[r]=i[r]);p&&p(t);while(d.length)d.shift()();return c.push.apply(c,s||[]),n()}function n(){for(var e,t=0;t<c.length;t++){for(var n=c[t],r=!0,a=1;a<n.length;a++){var u=n[a];0!==o[u]&&(r=!1)}r&&(c.splice(t--,1),e=i(i.s=n[0]))}return e}var r={},a={app:0},o={app:0},c=[];function u(e){return i.p+"static/js/"+({}[e]||e)+"."+{"chunk-190b9f3e":"18583a9f","chunk-2d0d3a85":"480a69fa","chunk-2d0d66f6":"b16d5c5b","chunk-2d0d79a0":"6a675e4f","chunk-2d0e148e":"c973a23d","chunk-2d21f24b":"2a6547d5","chunk-7c055edd":"859f6071","chunk-7d75888e":"2c893a14","chunk-a5b34e7c":"e7973061","chunk-afba42ec":"56b6c3b1"}[e]+".js"}function i(t){if(r[t])return r[t].exports;var n=r[t]={i:t,l:!1,exports:{}};return e[t].call(n.exports,n,n.exports,i),n.l=!0,n.exports}i.e=function(e){var t=[],n={"chunk-190b9f3e":1,"chunk-7c055edd":1,"chunk-7d75888e":1,"chunk-a5b34e7c":1,"chunk-afba42ec":1};a[e]?t.push(a[e]):0!==a[e]&&n[e]&&t.push(a[e]=new Promise((function(t,n){for(var r="static/css/"+({}[e]||e)+"."+{"chunk-190b9f3e":"beda8e88","chunk-2d0d3a85":"31d6cfe0","chunk-2d0d66f6":"31d6cfe0","chunk-2d0d79a0":"31d6cfe0","chunk-2d0e148e":"31d6cfe0","chunk-2d21f24b":"31d6cfe0","chunk-7c055edd":"40c48dda","chunk-7d75888e":"beda8e88","chunk-a5b34e7c":"58837e82","chunk-afba42ec":"beda8e88"}[e]+".css",o=i.p+r,c=document.getElementsByTagName("link"),u=0;u<c.length;u++){var s=c[u],f=s.getAttribute("data-href")||s.getAttribute("href");if("stylesheet"===s.rel&&(f===r||f===o))return t()}var d=document.getElementsByTagName("style");for(u=0;u<d.length;u++){s=d[u],f=s.getAttribute("data-href");if(f===r||f===o)return t()}var p=document.createElement("link");p.rel="stylesheet",p.type="text/css",p.onload=t,p.onerror=function(t){var r=t&&t.target&&t.target.src||o,c=new Error("Loading CSS chunk "+e+" failed.\n("+r+")");c.code="CSS_CHUNK_LOAD_FAILED",c.request=r,delete a[e],p.parentNode.removeChild(p),n(c)},p.href=o;var h=document.getElementsByTagName("head")[0];h.appendChild(p)})).then((function(){a[e]=0})));var r=o[e];if(0!==r)if(r)t.push(r[2]);else{var c=new Promise((function(t,n){r=o[e]=[t,n]}));t.push(r[2]=c);var s,f=document.createElement("script");f.charset="utf-8",f.timeout=120,i.nc&&f.setAttribute("nonce",i.nc),f.src=u(e);var d=new Error;s=function(t){f.onerror=f.onload=null,clearTimeout(p);var n=o[e];if(0!==n){if(n){var r=t&&("load"===t.type?"missing":t.type),a=t&&t.target&&t.target.src;d.message="Loading chunk "+e+" failed.\n("+r+": "+a+")",d.name="ChunkLoadError",d.type=r,d.request=a,n[1](d)}o[e]=void 0}};var p=setTimeout((function(){s({type:"timeout",target:f})}),12e4);f.onerror=f.onload=s,document.head.appendChild(f)}return Promise.all(t)},i.m=e,i.c=r,i.d=function(e,t,n){i.o(e,t)||Object.defineProperty(e,t,{enumerable:!0,get:n})},i.r=function(e){"undefined"!==typeof Symbol&&Symbol.toStringTag&&Object.defineProperty(e,Symbol.toStringTag,{value:"Module"}),Object.defineProperty(e,"__esModule",{value:!0})},i.t=function(e,t){if(1&t&&(e=i(e)),8&t)return e;if(4&t&&"object"===typeof e&&e&&e.__esModule)return e;var n=Object.create(null);if(i.r(n),Object.defineProperty(n,"default",{enumerable:!0,value:e}),2&t&&"string"!=typeof e)for(var r in e)i.d(n,r,function(t){return e[t]}.bind(null,r));return n},i.n=function(e){var t=e&&e.__esModule?function(){return e["default"]}:function(){return e};return i.d(t,"a",t),t},i.o=function(e,t){return Object.prototype.hasOwnProperty.call(e,t)},i.p="/",i.oe=function(e){throw console.error(e),e};var s=window["webpackJsonp"]=window["webpackJsonp"]||[],f=s.push.bind(s);s.push=t,s=s.slice();for(var d=0;d<s.length;d++)t(s[d]);var p=f;c.push([0,"chunk-vendors"]),n()})({0:function(e,t,n){e.exports=n("56d7")},1:function(e,t){},10:function(e,t){},2:function(e,t){},"255e":function(e,t,n){"use strict";n.d(t,"b",(function(){return r})),n.d(t,"c",(function(){return a})),n.d(t,"a",(function(){return o})),n.d(t,"d",(function(){return c})),n.d(t,"f",(function(){return u})),n.d(t,"e",(function(){return i}));var r="PROFILE_REQUEST_FETCHING",a="PROFILE_REQUEST_SUCCESS",o="PROFILE_REQUEST_ERROR",c="PROFILE_UPDATE",u="PROFILE_UPDATE_SUCCESS",i="PROFILE_UPDATE_ERROR"},"2edd":function(e,t,n){"use strict";n.d(t,"f",(function(){return r})),n.d(t,"d",(function(){return a})),n.d(t,"e",(function(){return o})),n.d(t,"g",(function(){return c})),n.d(t,"a",(function(){return u})),n.d(t,"b",(function(){return i})),n.d(t,"c",(function(){return s})),n.d(t,"k",(function(){return f})),n.d(t,"i",(function(){return d})),n.d(t,"j",(function(){return p})),n.d(t,"h",(function(){return h}));var r="AUTH_REQUEST",a="AUTH_REFRESH_REQUEST",o="AUTH_REFRESH_SUCCESS",c="AUTH_SUCCESS",u="AUTH_ERROR",i="AUTH_LOGOUT",s="AUTH_REFRESH_ERROR",f="FIRST_AUTH_REQUEST_SUCCESS",d="CREATE_USER_REQUEST",p="CREATE_USER_SUCCESS",h="CREATE_USER_ERROR"},3:function(e,t){},4:function(e,t){},5:function(e,t){},"56d7":function(e,t,n){"use strict";n.r(t);n("e260"),n("e6cf"),n("cca6"),n("a79d");var r,a,o,c,u=n("7a23"),i=(n("d3b7"),n("3ca3"),n("ddb0"),n("6c02")),s=n("66be"),f=n("5502"),d={profileStatus:"loading",profileUpdateStatus:"",profileInfo:null},p=d,h=n("ade3"),l=n("5530"),g=n("255e"),b=(r={},Object(h["a"])(r,g["b"],(function(e){e.profileStatus="loading"})),Object(h["a"])(r,g["c"],(function(e,t){var n=t.newProfileInfo;e.profileStatus="success",e.profileInfo=Object(l["a"])({},n)})),Object(h["a"])(r,g["a"],(function(e){e.profileStatus="error"})),Object(h["a"])(r,g["d"],(function(e){e.profileUpdateStatus="loading"})),Object(h["a"])(r,g["f"],(function(e,t){var n=t.newProfileInfo;e.profileUpdateStatus="success",e.profileInfo=Object(l["a"])({},n)})),Object(h["a"])(r,g["e"],(function(e){e.profileUpdateStatus="error"})),r),m=b,k=n("1da1"),v=(n("96cf"),n("bc3a")),S=n.n(v),O=n("14b7"),T=n.n(O),E=(a={},Object(h["a"])(a,g["b"],function(){var e=Object(k["a"])(regeneratorRuntime.mark((function e(t){var n,r,a,o,c;return regeneratorRuntime.wrap((function(e){while(1)switch(e.prev=e.next){case 0:if(n=t.commit,r=t.rootState,e.prev=1,a=r.tokens.accessToken,null!==a){e.next=5;break}return e.abrupt("return",n(g["a"],{}));case 5:return o=T.a.decode(a).user_id,n(g["b"]),e.next=9,S.a.get("/api/users/".concat(o),{headers:{"Content-Type":"application/json",Authorization:"Bearer ".concat(a)}});case 9:c=e.sent,console.log(c.data),n(g["c"],{newProfileInfo:c.data}),e.next=18;break;case 14:throw e.prev=14,e.t0=e["catch"](1),n(g["a"],e.t0),e.t0;case 18:case"end":return e.stop()}}),e,null,[[1,14]])})));return function(t){return e.apply(this,arguments)}}()),Object(h["a"])(a,g["d"],function(){var e=Object(k["a"])(regeneratorRuntime.mark((function e(t){var n,r,a,o,c;return regeneratorRuntime.wrap((function(e){while(1)switch(e.prev=e.next){case 0:if(n=t.commit,r=t.rootState,e.prev=1,a=r.tokens.accessToken,null!==a){e.next=5;break}return e.abrupt("return",n(g["a"],{}));case 5:return o=T.a.decode(a).user_id,n(g["d"]),e.next=9,S.a.get("/api/users/".concat(o),{headers:{"Content-Type":"application/json",Authorization:"Bearer ".concat(a)}});case 9:c=e.sent,console.log(c.data),n(g["f"],{newProfileInfo:c.data}),e.next=18;break;case 14:throw e.prev=14,e.t0=e["catch"](1),n(g["e"],e.t0),e.t0;case 18:case"end":return e.stop()}}),e,null,[[1,14]])})));return function(t){return e.apply(this,arguments)}}()),a),R=E,w={profileStatus:function(e){return e.profileStatus},profileInfo:function(e){return e.profileInfo},profileStats:function(e){return"success"===e.profileStatus?{money:e.profileInfo.money,energy:e.profileInfo.energy,health:e.profileInfo.health,status:e.profileStatus}:{status:e.profileStatus}}},P=w,j={namespaced:!0,state:p,mutations:m,getters:P,actions:R},_={accessToken:null,refreshToken:localStorage.getItem("refresh_token")||null,tokenStatus:"",firstRequestSuccess:!1,creatingUserStatus:null},y=_,U=n("2edd"),C=(o={},Object(h["a"])(o,U["f"],(function(e){e.tokenStatus="loading"})),Object(h["a"])(o,U["k"],(function(e){e.firstRequestSuccess=!0})),Object(h["a"])(o,U["d"],(function(e){e.tokenStatus="refreshing"})),Object(h["a"])(o,U["g"],(function(e,t){var n=t.accessToken,r=t.refreshToken;e.tokenStatus="success",e.accessToken=n,e.refreshToken=r})),Object(h["a"])(o,U["e"],(function(e,t){var n=t.accessToken;e.tokenStatus="success",e.accessToken=n})),Object(h["a"])(o,U["a"],(function(e){e.tokenStatus="error"})),Object(h["a"])(o,U["c"],(function(e){e.tokenStatus="error",e.accessToken=null,e.refreshToken=null,e.firstRequestSuccess=!1})),Object(h["a"])(o,U["b"],(function(e){e.tokenStatus="",e.accessToken=null,e.refreshToken=null,e.firstRequestSuccess=!1})),o),I=C,A=(c={},Object(h["a"])(c,U["i"],function(){var e=Object(k["a"])(regeneratorRuntime.mark((function e(t,n){var r,a;return regeneratorRuntime.wrap((function(e){while(1)switch(e.prev=e.next){case 0:return r=t.commit,e.prev=1,r(U["i"]),e.next=5,S.a.post("/api/login",{email:n.username,name:n.password,surname:n.password,password:n.password},{headers:{"Content-Type":"application/json"}});case 5:a=e.sent,r(U["g"],{accessToken:a.data.access,refreshToken:a.data.refresh}),r(U["j"]),localStorage.setItem("refresh_token",a.data.refresh),e.next=15;break;case 11:throw e.prev=11,e.t0=e["catch"](1),r(U["h"],e.t0),e.t0;case 15:case"end":return e.stop()}}),e,null,[[1,11]])})));return function(t,n){return e.apply(this,arguments)}}()),Object(h["a"])(c,U["f"],function(){var e=Object(k["a"])(regeneratorRuntime.mark((function e(t,n){var r,a;return regeneratorRuntime.wrap((function(e){while(1)switch(e.prev=e.next){case 0:return r=t.commit,e.prev=1,r(U["f"]),e.next=5,S.a.post("/api/login",{username:n.email,password:n.password},{headers:{"Content-Type":"application/json"}});case 5:a=e.sent,r(U["g"],{accessToken:a.data.access,refreshToken:a.data.refresh}),r(U["k"]),localStorage.setItem("refresh_token",a.data.refresh),e.next=15;break;case 11:throw e.prev=11,e.t0=e["catch"](1),r(U["a"],e.t0),e.t0;case 15:case"end":return e.stop()}}),e,null,[[1,11]])})));return function(t,n){return e.apply(this,arguments)}}()),Object(h["a"])(c,U["d"],function(){var e=Object(k["a"])(regeneratorRuntime.mark((function e(t){var n,r,a;return regeneratorRuntime.wrap((function(e){while(1)switch(e.prev=e.next){case 0:return n=t.commit,r=t.state,e.prev=1,n(U["d"]),e.next=5,S.a.post("/api/refresh-token",{refresh:r.refreshToken},{headers:{"Content-Type":"application/json"}});case 5:a=e.sent,n(U["e"],{accessToken:a.data.access}),r.firstRequestSuccess||n(U["k"]),e.next=15;break;case 10:throw e.prev=10,e.t0=e["catch"](1),n(U["c"]),localStorage.removeItem("refresh_token"),e.t0;case 15:case"end":return e.stop()}}),e,null,[[1,10]])})));return function(t){return e.apply(this,arguments)}}()),Object(h["a"])(c,U["b"],function(){var e=Object(k["a"])(regeneratorRuntime.mark((function e(t){var n,r;return regeneratorRuntime.wrap((function(e){while(1)switch(e.prev=e.next){case 0:return n=t.commit,r=t.state,e.prev=1,e.next=4,S.a.post("/api/logout",{refresh_token:r.refreshToken},{headers:{"Content-Type":"application/json"}});case 4:n(U["b"]),localStorage.removeItem("refresh_token"),e.next=12;break;case 8:throw e.prev=8,e.t0=e["catch"](1),n(U["a"]),e.t0;case 12:case"end":return e.stop()}}),e,null,[[1,8]])})));return function(t){return e.apply(this,arguments)}}()),c),x=A,L={isAuthenticated:function(e){return null!==e.refreshToken},creatingUserStatus:function(e){return e.creatingUserStatus}},q=L,H={namespaced:!0,state:y,mutations:I,getters:q,actions:x},F=new f["a"].Store({modules:{profile:j,tokens:H}}),B=[{path:s["a"].mainPage.path,component:function(){return n.e("chunk-7d75888e").then(n.bind(null,"cd56"))},children:[{path:s["a"].mainPage.path,component:function(){return n.e("chunk-7c055edd").then(n.bind(null,"e6dc"))}},{path:s["a"].mainPage.children.profilePage.path,component:function(){return n.e("chunk-2d21f24b").then(n.bind(null,"d922"))},meta:{requiresAuthentication:!0}},{path:s["a"].mainPage.children.pricesPage.path,component:function(){return n.e("chunk-2d0d66f6").then(n.bind(null,"7315"))}},{path:s["a"].mainPage.children.driversPage.path,component:function(){return n.e("chunk-2d0d3a85").then(n.bind(null,"5e65"))}},{path:s["a"].mainPage.children.newsPage.path,component:function(){return n.e("chunk-2d0e148e").then(n.bind(null,"7a7e"))}}]},{path:s["a"].authPage.path,component:function(){return n.e("chunk-a5b34e7c").then(n.bind(null,"2fef"))},children:[{path:s["a"].authPage.children.signInPage.path,component:function(){return n.e("chunk-190b9f3e").then(n.bind(null,"c790"))},meta:{requiresToBeLoggedOut:!0}},{path:s["a"].authPage.children.forgotPasswordPage.path,component:function(){return n.e("chunk-2d0d79a0").then(n.bind(null,"7809"))},meta:{requiresToBeLoggedOut:!0}},{path:s["a"].authPage.children.signUpPage.path,component:function(){return n.e("chunk-afba42ec").then(n.bind(null,"ccac"))},meta:{requiresToBeLoggedOut:!0}}]}],Q=Object(i["b"])("/"),N=Object(i["a"])({routes:B,history:Q});N.beforeEach((function(e,t,n){e.meta.requiresToBeLoggedOut?F.getters["tokens/isAuthenticated"]?n(s["a"].mainPage.path):n():e.meta.requiresAuthentication?F.getters["tokens/isAuthenticated"]?n():n(s["a"].authPage.children.signInPage.path):n()}));var D=N;function M(e,t,n,r,a,o){var c=Object(u["v"])("router-view");return Object(u["p"])(),Object(u["d"])(c)}var z={name:"App",components:{}};z.render=M;var G=z,J=(n("a766"),Object(u["c"])(G));J.use(D),J.use(F),J.mount("#app")},6:function(e,t){},"66be":function(e,t,n){"use strict";var r={mainPage:{path:"/",header:"Главная",children:{newsPage:{path:"/news"},pricesPage:{path:"/prices"},driversPage:{path:"/drivers"},profilePage:{path:"/profile",header:"Профиль",children:{editUser:{path:"/profile"},orderCar:{path:"/order-car"}}}}},authPage:{path:"/auth",header:"Авторизация",children:{signInPage:{path:"/auth/sign-in"},forgotPasswordPage:{path:"/auth/forgot-password"},signUpPage:{path:"/auth/sign-up"}}}};t["a"]=r},7:function(e,t){},8:function(e,t){},9:function(e,t){},a766:function(e,t,n){}});
//# sourceMappingURL=app.53641de8.js.map