
var pageVue = new Vue({
    el: '#pagePanel',

    data: {
        currentPage: 0,
        pages: [],
        screenshot_path:''
    },

    methods: {
        getPages: function (id) {
            this.currentPage = id
            axios.get(scanfUrl + "/page/" + id)
                .then((response) => {
                    this.pages = response.data
                }, (error) => {
                    alert("An error occured")
                })
            globalVue.$emit('eventPagesRefreshed')
        },

        getOnlyPath: function (url) {
            var el = document.createElement('a');
            el.href = url;
            return el.pathname + el.search
        },

        // getForms: function (page_id) {
        //     axios.get(scanfUrl + "/form/" + page_id)
        //         .then((response) => {
        //             console.log("in get forms", response.data)
        //             return response.data
        //         }, (error) => {
        //             alert("An error occured")
        //         })
        // },

        deletePage: function (id) {
            axios.delete(scanfUrl + "/page/" + id)
                .then((response) => {
                    this.getPages(this.currentPage)
                }, (error) => {
                    alert("An error occured")
                })
        },

        eventPageClick: function (page_id) {
            // globalVue.$emit('eventPageClick', page_id)
            axios.get(scanfUrl + "/page_screenshot/" + page_id)
                .then((response) => {
                    if(response.exists==true){
                        this.displayScreenshot(page_id)
                    }
                }, (error) => {
                    alert("An error occured")
                })
        },

        displayScreenshot: function(page_id){
            axios.get(scanfUrl + "/page/" + page_id)
                .then((response) => {
                    this.screenshot_path = response.screenshot_path
                }, (error) => {
                    alert("An error occured")
                })
        },

        eventFormClick: function (form_id) {
            globalVue.$emit('eventFormClick', form_id)
            console.log("form clicked", form_id)
        }
    },

    mounted() {
        globalVue.$on('eventWebsiteClick', function (website_id) {
            pageVue.getPages(website_id);
        })

        globalVue.$on('eventWebsitesRefreshed', () => {
            pageVue.getPages(pageVue.currentPage);
        })
    }
})
