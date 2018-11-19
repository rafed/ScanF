
var pageVue = new Vue({
    el: '#pages',

    data: {
        pages: []
    },

    methods: {
        getPages: function (id) {
            axios.get(scanfUrl + "/page/" + id)
                .then((response) => {
                    this.pages = response.data
                }, (error) => {
                    alert("An error occured")
                })
        },
    },

    mounted() {
        globalVue.$on('eventWebsiteClick', function(website_id) {
            console.log("event paisi!")
            pageVue.getPages(website_id);
        })
    }
})
