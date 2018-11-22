var globalVue = new Vue()


var websiteVue = new Vue({
    el: '#sitePanel',

    data: {
        inputUrl: '',
        loading: false,
        websites: '',
        nowactive: '',
        
        // Cookie
        cookies: '',
        cookieId:'',
        cookieName:'',
        cookieValue:'',
        cookieAddFlag:''
    },

    methods: {
        goCrawl: function (event) {
            if(this.inputUrl == ''){
                alert("Enter a URL");
                return
            }

            this.loading = true;
            document.body.style.cursor = 'wait';

            data = {
                'url': this.inputUrl
            }
            axios.post(scanfUrl + "/website", data)
                .then((response) => {
                    this.loading = false;
                    this.getWebsites()
                    document.body.style.cursor = 'default'
                }, (error) => {
                    this.loading = false;
                    alert(error.response.data.msg)
                    document.body.style.cursor = 'default'
                })
        },

        stopCrawl: function(){
            data = {
                'stop': 'stop'
            }
            axios.post(scanfUrl + "/website", data)
                .then((response)=>{
                    if(response.data.status == "ok"){
                        this.loading = false
                        document.body.style.cursor = 'default'
                        this.getWebsites()
                    }
                })
        },

        getWebsites: function () {
            axios.get(scanfUrl + "/website")
                .then((response) => {
                    this.websites = response.data
                }, (error) => {
                    alert("An error occured")
                })
            globalVue.$emit('eventWebsitesRefreshed')
        },
        
        deleteWebsite: function(id){
            axios.delete(scanfUrl + "/website/"+ id)
                .then((response) => {
                    this.getWebsites()
                }, (error) => {
                    alert("An error occured")
                })
        },

        eventWebsiteClick: function(website_id){
            this.nowactive = website_id
            this.getCookies(website_id)
            globalVue.$emit('eventWebsiteClick', website_id)
        },

        getCookies: function(website_id){
            axios.get(scanfUrl + "/cookie/" + website_id)
                .then((response) => {
                    this.cookies = response.data
                }, (error) => {
                    alert("An error occured")
                })
        },

        addCookie: function(){{
            if(this.nowactive==''){
                alert("Select a website first")
                return
            }

            this.cookieName = ''
            this.cookieValue = ''
            this.cookieAddFlag = true
            $("#cookieModal").modal();
            // document.getElementById("cookieModal").modal();
        }},

        addCookieRequest: function(){
            if(this.cookieName=='' || this.cookieValue==''){
                alert("Fill both name and cookie.")
                return
            }

            data = {
                'id':this.nowactive,    // website id
                'name':this.cookieName,
                'value':this.cookieValue
            }
            axios.post(scanfUrl + "/cookie", data)
                .then((response) => {
                    this.getCookies(this.nowactive)
                    console.log('lalalla')

                    this.cookieName=''
                    this.cookieValue=''
                }, (error) => {
                    alert("An error occured")
                })
        },

        updateCookie: function(cookie){
            this.cookieId = cookie.id
            this.cookieName = cookie.name
            this.cookieValue = cookie.value
            this.cookieAddFlag = false
        },

        updateCookieRequest: function(){
            if(this.cookieName=='' || this.cookieValue==''){
                alert("select a website and fill both name and cookie.")
                return
            }

            data = {
                'id': this.cookieId,    // cookie id
                'name': this.cookieName,
                'value': this.cookieValue
            }
            axios.put(scanfUrl + "/cookie", data)
                .then((response) => {
                    this.getCookies(this.nowactive)

                    this.cookieId = ''
                    this.cookieName=''
                    this.cookieValue=''
                }, (error) => {
                    alert("An error occured")
                })
        },

        deleteCookie: function(cookie){
            axios.delete(scanfUrl + "/cookie/"+ cookie.id)
                .then((response) => {
                    this.getCookies(this.nowactive)
                }, (error) => {
                    alert("An error occured")
                })
        }
    }
})
