
var testVue = new Vue({
    el: '#testPanel',

    data: {
        tests: []
    },

    methods: {
        getTests: function (id) {
            this.currentPage = id
            axios.get(scanfUrl + "/test/" + id)
                .then((response) => {
                    this.tests = response.data
                }, (error) => {
                    alert("An error occured")
                })
        },

        deleteTest: function (id) {
            axios.delete(scanfUrl + "/test/" + id)
                .then((response) => {
                    // emit event to injector panel
                }, (error) => {
                    alert("An error occured")
                })
        },

        eventTestClick: function(id){
            console.log("Test clicked", id)
        }
    },

    mounted() {
        globalVue.$on('eventFormClick', function (form_id) {
            testVue.getTests(form_id);
        })

        globalVue.$on('eventPagesRefreshed', () => {
            testVue.tests = []
        })
    }
})
