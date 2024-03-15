jQuery(document).ready(function(){	

    jQuery('[data-toggle="tooltip"]').tooltip();

    jQuery('.accardion-box h4').next('p').first().slideDown();
    jQuery('.accardion-box h4').click(function(){
        jQuery('.accardion-box h4').next('p').slideUp();
        jQuery(this).next('p').slideToggle();
    });
    
});	



