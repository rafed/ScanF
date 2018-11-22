
var attackVue = new Vue({
    el: '#injectionPanel',

    data: {
        sqlview: true,
        fields:[],
    },

    methods: {
        viewSql: function () {
            this.sqlview = true
        },

        viewXss: function(){
            this.sqlview = false
        },

        getFormFields: function (form_id) {
            axios.get(scanfUrl + "/field/" + form_id)
                .then((response) => {
                    this.fields = response.data
                    console.log(this.fields)
                }, (error) => {
                    alert("An error occured")
                })
        }
    },

    mounted() {
        globalVue.$on('eventFormClick', function (form_id) {
            attackVue.getFormFields(form_id);
        })
    }
})
