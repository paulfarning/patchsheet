module.exports = function(grunt) {
  grunt.initConfig({
    pkg: grunt.file.readJSON('package.json'),
    sass: {
      dist: {
        files: {
          'css/site.css' : 'scss/site.scss'
        }
      },
      site: {
        options: {
          style: 'compressed'
        },
        files: {
          'css/site.min.css' : 'scss/site.scss'
        }
      }
    },
    autoprefixer: {
      dist: {
        files: {
          'css/site.css': 'css/site.css'
        }
      },
      site: {
        files: {
          'css/site.min.css' : 'css/site.min.css'
        }
      }
    },
    watch: {
      css: {
        files: '**/*.scss',
        tasks: ['sass', 'autoprefixer']
      }
    },
    uglify: {
      site: {
        files: {
          'js/core.min.js': ['js/core.js']
        }
      }
    },
    concat: {
      site: {
        src: ['js/lib/jquery-2.1.1.min.js', 'js/lib/jquery-ui.min.js', 'js/lib/jquery-ui.touch-punch.min.js', 'js/lib/jquery.knob.min.js', 'js/core.min.js'],
        dest: 'js/site.min.js'
      }
    }
  });

  grunt.loadNpmTasks('grunt-autoprefixer');
  grunt.loadNpmTasks('grunt-contrib-sass');
  grunt.loadNpmTasks('grunt-contrib-watch');
  grunt.loadNpmTasks('grunt-contrib-concat');
  grunt.loadNpmTasks('grunt-contrib-uglify');

  grunt.registerTask('default', ['watch']);
  grunt.registerTask('build', ['sass:site', 'autoprefixer', 'uglify:site', 'concat:site'])

}
