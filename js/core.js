/**
 * @fileoverview Site core.
 * @author Paul Farning
 */



ps = {};
ps.sliderDefaults = {
  min: 0,
  max: 10,
  value: 0,
  step: .1,
  disabled: false
};
ps.knobDefaults = {
  min: 0,
  max: 100,
  value: 0,
  step: 1,
  readOnly: false,
  angleOffset: -135,
  angleArc: 270,
  fgColor: '#666',
  width: 90,
  thickness: .2,
  cursor: true
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
  this.initKnobs_();


}


ps.SetUp.prototype.view_ = function() {

  console.log('view');
  this.initSliders_();
  this.initKnobs_();

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


ps.SetUp.prototype.initKnobs_ = function() {

  $('.knob').each(function() {

    var knob = $(this);
    var min = knob.data('min') ? knob.data('min') : ps.knobDefaults.min;
    var max = knob.data('max') ? knob.data('max') : ps.knobDefaults.max;
    var step = knob.data('step') ? knob.data('step') : ps.knobDefaults.step;
    var readOnly = knob.data('readonly') ? knob.data('readonly') : ps.knobDefaults.readOnly;

    console.log(readOnly, knob.data('readonly'));

    knob.knob({
      min: min,
      max: max,
      step: step,
      readOnly: readOnly,
      angleArc: ps.knobDefaults.angleArc,
      angleOffset: ps.knobDefaults.angleOffset,
      fgColor: ps.knobDefaults.fgColor,
      width: ps.knobDefaults.width,
      thickness: ps.knobDefaults.thickness,
      cursor: ps.knobDefaults.cursor
    });

  });

};
