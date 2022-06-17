odoo.define(['appcof.btn_tree_get_token'
], function(require) {
    'use strict';
    var ListController = require('web.ListController');
    
    ListController.include({
        renderButtons: function ($node) {
            this._super.apply(this, arguments);            
            if (!this.noLeaf && this.hasButtons) {
                this.$buttons.on('click', '.o_list_button_multi_update', this._onBtnMultiUpdate.bind(this)); // add event listener
            }
        },
        _onBtnMultiUpdate: function (ev) {
            // we prevent the event propagation because we don't want this event to
            // trigger a click on the main bus, which would be then caught by the
            // list editable renderer and would unselect the newly created row
            if (ev) {
                ev.stopPropagation();
            }
            var self = this;
            return this._rpc({
                model: 'my.pet',
                method: 'btn_multi_update',
                args: [],
                context: this.initialState.context,
            }).then(function(result) {
                // location.reload();
                self.do_action(result);
            });
        },
    });
});