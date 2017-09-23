odoo.define('odoobro_website_module.customer_question', function (require) {
'use strict';

    var core = require('web.core');
    var ajax = require('web.ajax');
    var snippet_animation = require('web_editor.snippets.animation');

    var _t = core._t;


    snippet_animation.registry.customer_question_send = snippet_animation.Class.extend({
        selector: '.customer_question_form',

        start: function() {
            var self = this;
            self.$target.find('.customer_question_result').addClass("hidden");
            self.$target.find('.customer_question_form_send').removeClass("hidden");
            self.$target.find('.customer_question_form_send').on('click',function(e) {self.send(e);});
        },

        stop: function() {
            this.$target.find('input').off('click');
        },

        send: function(e) {
            e.preventDefault();  // Prevent the default submit behavior
            this.$target.find('.customer_question_form_send').off();  // Prevent users from crazy clicking

            var self = this;

            // Prepare form inputs
            self.form_fields = self.$target.serializeArray();
            _.each(self.$target.find('input[type=file]'), function(input) {
                $.each($(input).prop('files'), function(index, file) {
                    // Index field name as ajax won't accept arrays of files
                    // when aggregating multiple files into a single field value
                    self.form_fields.push({
                        name: input.name + '[' + index + ']',
                        value: file
                    });
                });
            });

            // Serialize form inputs into a single object
            // Aggregate multiple values into arrays
            var form_values = {};
            _.each(self.form_fields, function(input) {
                if (input.name in form_values) {
                    // If a value already exists for this field,
                    // we are facing a x2many field, so we store
                    // the values in an array.
                    if (Array.isArray(form_values[input.name])) {
                        form_values[input.name].push(input.value);
                    } else {
                        form_values[input.name] = [form_values[input.name], input.value];
                    }
                } else {
                    if (input.value != '') {
                        form_values[input.name] = input.value;
                    }
                }
            });

            // Overwrite form_values array with values from the form tag
            // Necessary to handle field values generated server-side, since
            // using t-att- inside a snippet makes it non-editable !
            for (var key in self.$target.data()) {
                if (_.str.startsWith(key, 'form_field_')){
                    form_values[key.replace('form_field_', '')] = self.$target.data(key);
                }
            }
            console.log(form_values);
            // Post form and handle result
            ajax.post(self.$target.attr('action') + (self.$target.data('force_action')||self.$target.data('model_name')), form_values)
            .then(function(result_data) {
                result_data = $.parseJSON(result_data);
                if(!result_data.id) {
                    alert("something wrong");
                } else {
                    // Success, redirect or update status
                	self.$target.find('.customer_question_form_send').addClass("hidden");
                	self.$target.find('.customer_question_result').removeClass("hidden");
                    // Reset the form
                    // self.$target[0].reset();
                }
            })
            .fail(function(result_data){
            	alert("something wrong");
            });
        },

    });
});
