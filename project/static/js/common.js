jQuery.fn.extend({ 
    date_time:function() {
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
        jQuery(this).html(result);
        //setTimeout('jQuery(this).date_time()','1000');
        return true;
    },

    category_hover:function(){
        jQuery(this).each(function(){
            var showtext = jQuery(this).attr("alt");
            jQuery(this).parent().hover(function(){
                jQuery("div."+showtext.toLowerCase()).show();
            },function(){
                jQuery("div."+showtext.toLowerCase()).hide();
            });
        });        
    }
});
