var globalVue = new Vue()


var websiteVue = new Vue({
    el: '#sitePanel',

    data: {
        inputUrl: '',
        loading: false,
        websites: '',
        cookies: '',
        pages: ''
    },

    methods: {
        goCrawl: function (event) {
            if(this.inputUrl == ''){
                alert("Enter a URL");
                return
            }

            this.loading = true;
            data = {
                'url': this.inputUrl
            }
            axios.post(scanfUrl + "/website", data)
                .then((response) => {
                    this.loading = false;
                    this.getWebsites()
                }, (error) => {
                    this.loading = false;
                })
        },

        getWebsites: function () {
            axios.get(scanfUrl + "/website")
                .then((response) => {
                    this.websites = response.data
                }, (error) => {
                    alert("An error occured")
                })
        },

        eventWebsiteClick: function(website_id){
            globalVue.$emit('eventWebsiteClick', website_id)
            // pageVue.getPages(website_id);
        }
    }
})
