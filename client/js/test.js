
var testVue = new Vue({
    el: '#testPanel',

    data: {
        // t:{
        //     id:1,
        //     form_id:1,
        //     type:'sqli',
        //     html_output_path:'file_12093.html',
        //     screenshot_path:'img_12309.png',
        //     time:'13:45',
        //     duration: '3s',
        //     result: 'vulnerable'
        // },
        tests: [],
        nowactive:''
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
                    if(this.nowactive==null){
                        this.tests = []
                    }
                    else {
                        this.getTests(nowactive.form_id)
                    }
                    // emit event to injector panel////////////
                }, (error) => {
                    alert("An error occured")
                })
        },

        eventTestClick: function(test){
            this.nowactive = test
            globalVue.$emit('eventTestClick', test)
        }
    },

    mounted() {
        globalVue.$on('eventFormClick', function (form_id) {
            testVue.getTests(form_id);
        })

        // globalVue.$on('eventPagesRefreshed', () => {
        //     testVue.tests = []
        // })
    }
})
