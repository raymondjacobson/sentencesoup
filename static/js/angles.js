var sentenceSoupApp = angular.module('sentenceSoupApp', ['ngRoute']);

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
    .otherwise({
      templateUrl: 'static/partials/_404.html',
      controller: '404Ctrl'
    })
});

// controllers for routes
sentenceSoupApp.controller('defaultCtrl', function($scope) {
  $scope.message = 'default';
});
sentenceSoupApp.controller('storyCtrl', function($scope) {
  $scope.message = 'story';
});
sentenceSoupApp.controller('404Ctrl', function($scope) {
  $scope.message = '404 - an error';
});