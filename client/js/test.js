
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
        nowactive:'',
        currentForm: '',
        tab:''
    },

    methods: {
        getTests: function (id) {
            this.currentForm = id
            axios.get(scanfUrl + "/test/" + id)
                .then((response) => {
                    this.tests = response.data
                    console.log(response.data)
                }, (error) => {
                    alert("An error occured")
                })
        },

        eventTestClick: function(test){
            this.nowactive = test
            globalVue.$emit('eventTestClick', test)
        },

        deleteTest: function (id) {
            axios.delete(scanfUrl + "/test/" + id)
                .then((response) => {
                    this.getTests(this.currentForm)
                }, (error) => {
                    alert("An error occured")
                })
        },
    },

    mounted() {
        globalVue.$on('eventFormClick', function (form_id) {
            testVue.getTests(form_id)
            if(testVue.tab == null) testVue.tab = 'sql'
        })

        globalVue.$on('loadTests', function(form_id){
            testVue.getTests(form_id)
            if(testVue.tab == null) testVue.tab = 'sql'
        })

        globalVue.$on('viewchanged', (type) => {
            testVue.tab = type
        })
    }
})
