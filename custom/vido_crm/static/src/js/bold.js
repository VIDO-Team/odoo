odoo.define(
    'mystudent.bold'
, function(require) {
    'use strict';
    var basic_fields = require('web.basic_fields');
    var registry = require('web.field_registry');

    var BoldWidget = basic_fields.FieldChar.extend({
        _renderReadonly: function () {
            this._super();
            var old_html_render = this.$el.html();
            var new_html_render = '<b style="color:red;">' + old_html_render + '</b>'
            this.$el.html(new_html_render);
        },
    });
    registry.add('bold_red', BoldWidget);
});