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
    
    jQuery("div.homeicon img#home_icon").hover(function(){
        jQuery("#dashboard").fadeIn(500);
    }, function(){
        jQuery("#dashboard").fadeOut(500);
    });
    
    jQuery("div#dashboard").hover(function(){
        jQuery(this).stop().animate({opacity:'100'});
//        jQuery(this).show();
    },function(){
        jQuery(this).fadeOut(500);
    });
    
})
