/** Renders the color picker used e.g. in the tool form **/
import Utils from "utils/utils";
import Ui from "mvc/ui/ui-misc";

/** Renders an input element used e.g. in the tool form */
export default Backbone.View.extend({
    initialize: function (options) {
        this.model =
            (options && options.model) ||
            new Backbone.Model({
                value: { src: "json", value: null, representation: "null" },
            }).set(options);
        this.$el = $("<div><p>moo cow</p></div>").addClass("ui-field");
        console.log(this.model.get("value"));
        var menuButton = new Ui.ButtonMenu({
            id: "options",
            icon: "fa-caret-down",
            title: "Input Type",
            tooltip: "View available input type options",
        });
        menuButton.addMenu({
            title: "Integer",
            onclick: () => {
                this._changeType("integer");
            },
        });
        menuButton.addMenu({
            title: "Leave Unselected",
            onclick: () => {
                this._changeType("null");
            },
        });
        this.$menuButton = menuButton;
        this.$inputDiv = $("<div/>").addClass("select-input");

        this.$el.append(menuButton.$el);
        this.$el.append(this.$inputDiv);
        this.setElement(this.$el);
        this.listenTo(this.model, "change", this.render, this);
        this.render();
    },
    value: function (new_val) {
        var options = this.model.attributes;
        if (new_val) {
            this.model.set("value", new_val);
            this.model.trigger("change");
            options.onchange(new_val);
        }
        return this.model.get("value");
    },
    render: function () {
        const value = this.model.get("value");
        const rep = value.representation;
        if (rep == "null") {
            this.$inputDiv.html($("<p>No value selected (null)</p>"));
        } else if (rep == "integer") {
            const tagName = this.model.get("area") ? "textarea" : "input";
            this.$inputDiv.html($(`<${tagName} value="${value.value}"/>`));
            console.log(this.$inputDiv.find("input"));
            this.$inputDiv.find("input").on("change", () => {
                this._onchange();
            });
        }
        return this;
    },
    _changeType: function (representation) {
        const previousValue = this.model.get("value");
        const previousRawValue = previousValue.value;
        if (representation == "null") {
            this.model.set("value", { src: "json", value: null, representation: "null" });
        } else if (representation == "integer") {
            var value = parseInt(previousRawValue);
            if (isNaN(value)) {
                value = 0;
            }
            this.model.set("value", { src: "json", value: 0, representation: "integer" });
        }
    },
    _rawValue: function (previousValue) {
        const rep = previousValue.representation;
        let rawVal;
        if (rep == "null") {
            rawVal = null;
        } else if (rep == "integer") {
            rawVal = parseInt(this.$inputDiv.find("input").val());
        }
        console.log("_rawValue returning " + rawVal);
        return rawVal;
    },
    _onchange: function () {
        const previousValue = this.model.get("value");
        const newValue = this._rawValue(previousValue);
        previousValue["value"] = newValue;
        this.value(previousValue);
        this.model.get("onchange") && this.model.get("onchange")(this.model.get("value"));
    },
});
