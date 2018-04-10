var gulp = require('gulp')
var sass = require('gulp-sass')
var concat = require('gulp-concat')
var rename = require('gulp-rename')
var autoprefixer = require('autoprefixer')
var postcss = require('gulp-postcss')

gulp.task('sass', function(){
  return gulp.src('databse/static/scss/*.scss').pipe(sass()).pipe(gulp.dest('databse/static/css'));
});

gulp.task('vendor', function() {
// Bootstrap
  gulp.src([
      './node_modules/bootstrap/dist/**/*',
      '!./node_modules/bootstrap/dist/css/bootstrap-grid*',
      '!./node_modules/bootstrap/dist/css/bootstrap-reboot*'
    ])
    .pipe(gulp.dest('./vendor/bootstrap'))
// jQuery
  gulp.src([
      './node_modules/jquery/dist/*',
      '!./node_modules/jquery/dist/core.js'
    ])
    .pipe(gulp.dest('./databse/static/jquery'))

})

gulp.task('scripts', function(){
  return gulp.src('databse/static/js/*.js').pipe(concat('all.js')).pipe(gulp.dest('databse/static/js'));
});

gulp.task('css', function(){
  var processors = [
    autoprefixer({browsers:['last 1 version']}),
  ];
  return gulp.src('databse/static/css/*.css').pipe(postcss(processors)).pipe(gulp.dest('databse/static/css'));
});

gulp.task('watch', function(){
  gulp.watch('databse/static/js/*.js', ['scripts']);
  gulp.watch('databse/static/scss/*.scss', ['sass']);
  gulp.watch('databse/static/css/*.css', ['css']);
});

gulp.task('default', ['sass', 'css', 'scripts', 'watch']);
