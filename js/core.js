/**
 * @fileoverview Site core.
 * @author Paul Farning
 */



ps = {};
ps.sliderDefaults = {
  min: 0,
  max: 10,
  value: 0,
  step: 1,
  disabled: false
};

ps.SetUp = function(pageName) {

  this.pageName_ = pageName + '_';

  this.init_();

};


ps.SetUp.prototype.init_ = function() {

  if (('undefined' !== typeof this.pageName_) && (this[this.pageName_])) {
    this[this.pageName_]();
  }

};


ps.SetUp.prototype.create_ = function() {

  console.log('create');
  this.initSliders_();


}


ps.SetUp.prototype.view_ = function() {

  console.log('view');
  this.initSliders_();

}


ps.SetUp.prototype.initSliders_ = function() {

  $('.slider-vertical').each(function() {

    var slider = $(this);
    var field = slider.parent().find('input').first();
    var min = slider.data('min') ? slider.data('min') : ps.sliderDefaults.min;
    var max = slider.data('max') ? slider.data('max') : ps.sliderDefaults.max;
    var value = slider.data('value') ? slider.data('value') : ps.sliderDefaults.value;
    var step = slider.data('step') ? slider.data('step') : ps.sliderDefaults.step;
    var disabled = slider.data('disabled') ? slider.data('disabled') : ps.sliderDefaults.disabled;

    slider.slider({
      orientation: 'vertical',
      min: min,
      max: max,
      value: value,
      step: step,
      disabled: disabled,
      slide: function(event, ui) {
        field.val(ui.value);
      }
    });

    field.val(slider.slider('value'));

  });

};
