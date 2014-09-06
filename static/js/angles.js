function updateScroll(element){
  var element = document.getElementById(element);
  element.scrollTop = element.scrollHeight;
}

var sentenceSoupApp = angular.module('sentenceSoupApp', ['firebase', 'ngRoute']);

// helpers
var addScript = function(script_name) {
  var s = document.createElement('script');
  s.src = script_name;
  document.body.appendChild(s);
}

// configure angular routes
sentenceSoupApp.config(function($routeProvider) {
  $routeProvider
    .when('/', {
      templateUrl: '/static/partials/_story.html',
      controller: 'storyCtrl'
    })
    .when('/art', {
      templateUrl: '/static/partials/_art.html',
      controller: 'artCtrl'
    })

    .otherwise({
      templateUrl: 'static/partials/_404.html',
      controller: '404Ctrl'
    })
});

// controllers for routes
sentenceSoupApp.controller('defaultCtrl', function($scope) {
});
sentenceSoupApp.controller('storyCtrl', ["$scope", "$firebase",
  function($scope, $firebase) {
    var ref = new Firebase("https://sentencesoup.firebaseio.com/story");
    var sync = $firebase(ref);
    var syncObject = sync.$asObject();
    syncObject.$bindTo($scope, "story");
    $scope.$watch("story", function(value) {
      var element = document.getElementById("story");
      setTimeout(function() {
        updateScroll("story");
      });
    });
  }
]);
sentenceSoupApp.controller('artCtrl', ["$scope", "$firebase",
  function($scope, $firebase) {
    var ref = new Firebase("https://sentencesoup.firebaseio.com/story");
    var sync = $firebase(ref);
    var syncObject = sync.$asObject();
    syncObject.$bindTo($scope, "story");
  }
]);
sentenceSoupApp.controller('404Ctrl', function($scope) {
  $scope.message = '404 - an error';
});