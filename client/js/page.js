
var pageVue = new Vue({
    el: '#pagePanel',

    data: {
        currentWebsite: 0,
        nowactive:'',
        pages: [],
        screenshot_path: '',

        modalDisplay: 'none',
        modalImgSrc: '',
        modalCaption:''
    },

    methods: {
        getPages: function (id) {
            this.currentWebsite = id
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

        deletePage: function (id) {
            axios.delete(scanfUrl + "/page/" + id)
                .then((response) => {
                    this.getPages(this.currentWebsite)
                }, (error) => {
                    alert("An error occured")
                })
        },

        eventPageClick: function (page_id) {
            document.body.style.cursor = 'wait';

            axios.get(scanfUrl + "/page_screenshot/" + page_id)
                .then((response) => {
                    document.body.style.cursor = 'default'
                    this.displayScreenshot(response.data)
                }, (error) => {
                    document.body.style.cursor = 'default'
                    alert("An error occured")
                })
        },

        displayScreenshot: function (page) {
            this.modalDisplay = "block"
            this.modalImgSrc = page.screenshot_path
            this.modalCaption = page.url
            console.log(page.screenshot_path)
        },

        closeScreenshot: function(){
            this.modalDisplay = "none"
        },

        eventFormClick: function (form) {
            this.nowactive = form.page_id
            globalVue.$emit('eventFormClick', form.id)
            console.log("form clicked", form.id)
        }
    },

    mounted() {
        globalVue.$on('eventWebsiteClick', function (website_id) {
            pageVue.getPages(website_id);
        })

        globalVue.$on('eventWebsitesRefreshed', () => {
            pageVue.getPages(pageVue.currentWebsite);
        })
    }
})
