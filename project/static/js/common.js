    function date_time(id) {
        date = new Date;
        year = date.getFullYear();
        month = date.getMonth();
        months = new Array('Jan', 'Febr', 'Mar', 'Apr', 'May', 'June', 'Jul', 'Aug', 'Sept', 'Oct', 'Nov', 'Dec');
        d = date.getDate();
        day = date.getDay();
        days = new Array('Sun', 'Mon', 'Tues', 'Wedn', 'Thur', 'Fri', 'Sat');
        h = date.getHours();
        if(h<10)
        {
            h = "0"+h;
        }
        m = date.getMinutes();
        if(m<10)
        {
            m = "0"+m;
        }
        s = date.getSeconds();
        if(s<10)
        {
            s = "0"+s;
        }
        result = ''+days[day]+' '+months[month]+' '+d+' '+year+' '+h+':'+m+':'+s;
        jQuery(id).html(result);
        setTimeout(function(){date_time(id)},'1000');
        return true;
    }

jQuery(document).ready(function(){
        jQuery("#category img, #dashboard img").each(function(){
            var showtext = jQuery(this).attr("alt");
            jQuery(this).parent().hover(function(){
                jQuery("div."+showtext.toLowerCase()).show();
            },function(){
                jQuery("div."+showtext.toLowerCase()).hide();
            });
        });
    
    jQuery(".fancybox_dash").fancybox({
        padding: [10,0,5,0],

        openEffect: "elastic",
        openSpeed: 250,
        
        closeEffect: "elastic",
        closeSpeed: 250,
        
        closeClick: true,

        helpers:{
            title:{
                type: 'float',// 'float', 'inside', 'outside' or 'over'
            },
            overlay : {
                closeClick : true,  // if true, fancyBox will be closed when user clicks on the overlay
                speedOut   : 200,   // duration of fadeOut animation
                showEarly  : true,  // indicates if should be opened immediately or wait until the content is ready
                css        : {
                    'background':'rgba(200,200,200,0.5)',
                },    // custom CSS properties
                locked     : true   // if true, the content will be locked into overlay
            },
        },

    });
    
    jQuery(".fancybox_new").fancybox({
        openEffect: 'elastic',
        openSpeed: 300,
        
        closeEffect:'elastic',
        closeSpeed:300,
        
        closeClick:false,
        
        helpers:{
            overlay:{
                closeClick:true,
                speedOut:200,
                showEarly: true,
                css: {
                    'background':'rgba(200,200,200,0.5)',
                    },
                locked: true
            },
        
        },

        autoSize: false,
        width: 600,
        maxHeight:500,
        beforeShow: function(){
            initTinyMCE();
        }
    });

    jQuery( '.navigation ul' ).lavaLamp({ startItem: 0 });
});

function initTinyMCE(){
    tinymce.init({
        selector:"#ar_text",
        theme:"modern",
        height:220,
        plugins: [
            "advlist autolink lists link image charmap print preview hr anchor pagebreak",
            "searchreplace wordcount visualblocks visualchars code fullscreen",
            "insertdatetime media nonbreaking save table contextmenu directionality",
            "emoticons template paste textcolor openmanager"
        ],
        toolbar: "insertfile undo redo | styleselect | bold italic | alignleft aligncenter alignright alignjustify | bullist numlist outdent indent | link image | print preview media | forecolor backcolor emoticons | ibrowser",
        theme_advanced_buttons3_add: "ibrowser",
        image_advtab: true,
        file_browser_callback: "openmanager",
        open_manager_upload_path: '../../../../media/',
        templates: [
            {title: 'Test template 1', content: 'Test 1'},
            {title: 'Test template 2', content: 'Test 2'}
        ],
        theme_advanced_toolbar_location : "top"
    });
}
