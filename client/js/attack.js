
var attackVue = new Vue({
    el: '#injectionPanel',

    data: {
        currentview: '',
        fields: [],

        form_id: 0,

        sqlPayload: '',
        sqlis: [],
        sqliTestResult: null,

        xssPayload: '',
        xsss: [],
        xssTestResult: null,

        // Screenshot stuff
        modalDisplay: 'none',
        modalImgSrc: '',
    },

    methods: {
        viewSql: function () {
            this.currentview = 'sql'
            globalVue.$emit('viewchanged', 'sql')
        },

        viewXss: function () {
            this.currentview = 'xss'
            globalVue.$emit('viewchanged', 'xss')
        },

        getFormFields: function (form_id) {
            axios.get(scanfUrl + "/field/" + form_id)
                .then((response) => {
                    this.fields = response.data
                    console.log(this.fields)
                }, (error) => {
                    alert("An error occured")
                })
        },

        autoXSSAttack: function(){
            data = {
                'form_id': this.form_id,
                'payload': this.xssPayload
            }

            document.body.style.cursor = 'wait'
            axios.post(scanfUrl + "/autoxssattack", data)
                .then((response) => {
                    globalVue.$emit('loadTests', this.form_id)
                    document.body.style.cursor = 'default'
                })
        },

        autoSQLiAttack: function () {
            data = {
                'form_id': this.form_id,
                'payload': this.sqlPayload
            }
            
            document.body.style.cursor = 'wait'
            axios.post(scanfUrl + "/autosqlattack", data)
                .then((response) => {
                    globalVue.$emit('loadTests', this.form_id)
                    document.body.style.cursor = 'default'
                })
        },

        manualSQLiAttack: function () {
            new_data = {}

            for(var i=0; i<this.fields.length; i++){
                new_data[this.fields[i].name] = this.fields[i].default_value
            }

            data = {
                'form_id': this.form_id,
                'data': JSON.stringify(new_data)
            }
            
            document.body.style.cursor = 'wait'
            axios.post(scanfUrl + "/manualsqlattack", data)
                .then((response) => {
                    globalVue.$emit('loadTests', this.form_id)
                    document.body.style.cursor = 'default'
                })
        },

        displayScreenshot: function (path) {
            this.modalDisplay = "block"
            this.modalImgSrc = path
            console.log("bal amar")
        },

        closeScreenshot: function(){
            this.modalDisplay = "none"
        },

        formatDuration: function(duration){
            return Number(duration).toFixed(3) + 's'
        }
    },

    created() {
        axios.get('http://localhost:5000/api' + "/sql")
            .then((response) => {
                this.sqlis = response.data
            }, (error) => {
                alert("An error occured")
            })

        axios.get('http://localhost:5000/api' + "/xss")
            .then((response) => {
                this.xsss = response.data
            }, (error) => {
                alert("An error occured")
            })
    },

    mounted() {
        globalVue.$on('eventFormClick', function (form_id) {
            if (attackVue.currentview == '') attackVue.currentview = 'sql'
            globalVue.$emit('viewchanged', 'sql')

            attackVue.getFormFields(form_id);
            attackVue.form_id = form_id

            attackVue.sqliTestResult = null
        }),

        globalVue.$on('eventTestClick', function (test) {
            console.log(test.type)
            if(test.type == 'sql'){
                attackVue.sqliTestResult = test

                jsonObject = JSON.parse(test.input_json)
                for (var key in jsonObject) {
                    for (var i=0; i<attackVue.fields.length; i++) {
                        field = attackVue.fields[i]
                        if (field.name == key) {
                            attackVue.fields[i].default_value = jsonObject[key]
                        }
                    }
                }
            }
            else if (test.type == 'xss'){
                attackVue.xssTestResult = test
            }
            
        })
    }
})
