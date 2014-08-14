module.exports = function(grunt) {
  grunt.initConfig({
    pkg: grunt.file.readJSON('package.json'),

    autoprefixer: {
      dist: {
        files: {
          'css/site.min.css': 'css/site.min.css'
        }
      }
    },

    concat: {
      site: {
        src: [
          'js/lib/jquery-2.1.1.min.js',
          'js/lib/jquery-ui.min.js',
          'js/lib/jquery-ui.touch-punch.min.js',
          'js/lib/jquery.knob.min.js',
          'js/core.min.js'
        ],
        dest: 'js/site.min.js'
      }
    },

    jshint: {
      options: {
        force: true,
        globals: {
          jQuery: true
        },
        jquery: true,
        maxlen: 100
      },
      all: ['Gruntfile.js', 'js/core.js']
    },

    sass: {
      dist: {
        options: {
          style: 'compressed'
        },
        files: {
          'css/site.min.css' : 'scss/site.scss'
        }
      }
    },

    uglify: {
      site: {
        files: {
          'js/core.min.js': ['js/core.js']
        }
      }
    },

    watch: {
      css: {
        files: ['**/*.scss'],
        tasks: ['sass', 'autoprefixer']
      },
      scripts: {
        files: ['Gruntfile.js', 'js/core.js'],
        tasks: ['jshint']
      }
    }
  });

  grunt.loadNpmTasks('grunt-autoprefixer');
  grunt.loadNpmTasks('grunt-contrib-concat');
  grunt.loadNpmTasks('grunt-contrib-jshint');
  grunt.loadNpmTasks('grunt-contrib-sass');
  grunt.loadNpmTasks('grunt-contrib-uglify');
  grunt.loadNpmTasks('grunt-contrib-watch');

  grunt.registerTask('default', ['watch']);
  grunt.registerTask('build', [
    'sass',
    'autoprefixer',
    'jshint:site',
    'uglify:site',
    'concat:site'
  ]);

};
