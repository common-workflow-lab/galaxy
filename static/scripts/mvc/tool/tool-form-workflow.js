define(["utils/utils","mvc/tool/tool-form-base"],function(a,b){var c=b.extend({initialize:function(c){var d=this;return this.hasLabelListeners=!1,this.node=c.node,this.node?(this.post_job_actions=this.node.post_job_actions||{},c=a.merge(c,{text_enable:"Set in Advance",text_disable:"Set at Runtime",narrow:!0,initial_errors:!0,sustain_version:!0,cls:"ui-portlet-narrow",update_url:Galaxy.root+"api/workflows/build_module",update:function(a){d.initializeLabelListener(),d.node.update_field_data(a),d.errors(a&&a.tool_model)}}),a.deepeach(c.inputs,function(b){b.type&&(-1!=["data","data_collection"].indexOf(b.type)?(b.type="hidden",b.info="Data input '"+b.name+"' ("+a.textify(b.extensions&&b.extensions.toString())+")",b.value=null):(b.collapsible_value={__class__:"RuntimeValue"},b.is_workflow=b.options&&0==b.options.length||-1!=["integer","float"].indexOf(b.type)))}),a.deepeach(c.inputs,function(a){"conditional"==a.type&&(a.test_param.collapsible_value=void 0)}),this._makeSections(c),void b.prototype.initialize.call(this,c)):void Galaxy.emit.debug("tool-form-workflow::initialize()","Node not found in workflow.")},initializeLabelListener:function(){var a=this;if(this.hasLabelListeners===!1){this.hasLabelListeners=[];{var b=_.where(this.options.inputs,{outputSection:!0});b.map(function(b){var c=b.id,d=b.outputId,e=$("#"+c),f=e.find(".section-row").first(),g=f.find("input")[0];$(g).bind("input propertychange",function(){var b=$(g).val(),c=a.node.app.workflow;c.attemptUpdateOutputLabel(a.node,d,b)})})}}},_makeSections:function(b){var c=b.inputs,d=b.datatypes;c[a.uid()]={label:"Annotation / Notes",name:"annotation",type:"text",area:!0,help:"Add an annotation or note for this step. It will be shown with the workflow.",value:this.node.annotation};var e=this.node.output_terminals&&Object.keys(this.node.output_terminals)[0];if(e){c[a.uid()]={name:"pja__"+e+"__EmailAction",label:"Email notification",type:"boolean",value:String(Boolean(this.post_job_actions["EmailAction"+e])),ignore:"false",help:"An email notification will be send when the job has completed.",payload:{host:window.location.host}},c[a.uid()]={name:"pja__"+e+"__DeleteIntermediatesAction",label:"Output cleanup",type:"boolean",value:String(Boolean(this.post_job_actions["DeleteIntermediatesAction"+e])),ignore:"false",help:"Delete intermediate outputs if they are not used as input for another job."};for(var f in this.node.output_terminals)c[a.uid()]=this._makeSection(f,d)}},_makeSection:function(a,b){function c(b,d){d=d||[],d.push(b);for(var e in b.inputs){var f=b.inputs[e],h=f.action;if("Label"==h){var i=g.node.getWorkflowOutput(a);f.value=i?i.label||"":""}else if(h){if(f.name="pja__"+a+"__"+f.action,f.pja_arg&&(f.name+="__"+f.pja_arg),f.payload)for(var j in f.payload){var k=f.payload[j];f.payload[f.name+"__"+j]=k,delete k}var l=g.post_job_actions[f.action+a];if(l){for(var m in d)d[m].expanded=!0;f.value=f.pja_arg?l.action_arguments&&l.action_arguments[f.pja_arg]||f.value:"true"}}f.inputs&&c(f,d.slice(0))}}var d=[],e=[];for(key in b)d.push({0:b[key],1:b[key]});for(key in this.node.input_terminals)e.push(this.node.input_terminals[key].name);d.sort(function(a,b){return a.label>b.label?1:a.label<b.label?-1:0}),d.unshift({0:"Sequences",1:"Sequences"}),d.unshift({0:"Roadmaps",1:"Roadmaps"}),d.unshift({0:"Leave unchanged",1:"__empty__"});var f={title:"Configure Output: '"+a+"'",type:"section",flat:!0,outputSection:!0,outputId:a,inputs:[{action:"Label",label:"Label",type:"text",value:"",ignore:"",help:"This will provide a short name to describe the output - this must be unique across workflows."},{action:"RenameDatasetAction",pja_arg:"newname",label:"Rename dataset",type:"text",value:"",ignore:"",help:'This action will rename the output dataset. Click <a hr\nef="https://wiki.galaxyproject.org/Learn/AdvancedWorkflow/Variables">here</a> for more info\nrmation. Valid inputs are: <strong>'+e.join(", ")+"</strong>."},{},{action:"ChangeDatatypeAction",pja_arg:"newtype",label:"Change datatype",type:"select",ignore:"__empty__",value:"__empty__",options:d,help:"This action will change the datatype of the output to the indicated value."},{action:"TagDatasetAction",pja_arg:"tags",label:"Tags",type:"text",value:"",ignore:"",help:"This action will set tags for the dataset."},{title:"Assign columns",type:"section",flat:!0,inputs:[{action:"ColumnSetAction",pja_arg:"chromCol",label:"Chrom column",type:"integer",value:"",ignore:""},{action:"ColumnSetAction",pja_arg:"startCol",label:"Start column",type:"integer",value:"",ignore:""},{action:"ColumnSetAction",pja_arg:"endCol",label:"End column",type:"integer",value:"",ignore:""},{action:"ColumnSetAction",pja_arg:"strandCol",label:"Strand column",type:"integer",value:"",ignore:""},{action:"ColumnSetAction",pja_arg:"nameCol",label:"Name column",type:"integer",value:"",ignore:""}],help:"This action will set column assignments in the output dataset. Blank fields are ignored."}]},g=this;return c(f),f}});return{View:c}});
//# sourceMappingURL=../../../maps/mvc/tool/tool-form-workflow.js.map