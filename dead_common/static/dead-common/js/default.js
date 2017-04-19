/**
 * After AJAX
 */
$(document).ajaxStop(function() {
    dead_js_utilities.after_ajax();
});

/**
 * Document ready
 */
$(document).ready(function() {
    dead_js_utilities.init();
});
