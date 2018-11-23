
var attackVue = new Vue({
    el: '#injectionPanel',

    data: {
        currentview: '',
        fields: [],

        sqliSelected: '',
        sqlis: []
    },

    methods: {
        viewSql: function () {
            this.currentview = 'sql'
        },

        viewXss: function () {
            this.currentview = 'xss'
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

        autoSQLiAttack: function(){

        }
    },

    created() {
        axios.get('http://localhost:5000/api' + "/sql")
            .then((response) => {
                this.sqlis = response.data
            }, (error) => {
                alert("An error occured")
            })
    },

    mounted() {
        globalVue.$on('eventFormClick', function (form_id) {
            if(attackVue.currentview=='') attackVue.currentview='sql'
            attackVue.getFormFields(form_id);
        })
    }
})
