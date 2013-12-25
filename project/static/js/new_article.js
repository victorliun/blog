function initTinyMCE(){
    tinymce.init({
        selector:"#article_content",
        theme:"modern",
        height:220,
        plugins: [
            "advlist autolink lists link image charmap print preview hr anchor pagebreak",
            "searchreplace wordcount visualblocks visualchars code fullscreen",
            "insertdatetime media nonbreaking save table contextmenu directionality",
            "emoticons template paste textcolor moxiemanager"
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


jQuery(document).ready(function(){

    initTinyMCE();

})
