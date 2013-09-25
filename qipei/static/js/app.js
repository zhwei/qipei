/**
 * Created with PyCharm.
 * User: zhwei
 * Date: 8/15/13
 * Time: 8:44 PM
 * To change this template use File | Settings | File Templates.
 */

$(function(){
    $('#uploadAvatarBtnLayout button').addClass('button-deep-color');

    $('#uploadAvatarInputFile').mouseover(function(){
        $('#uploadAvatarBtnLayout button').removeClass('button-deep-color').addClass('button-light-color');
    }).mouseout(function(){
        $('#uploadAvatarBtnLayout button').removeClass('button-light-color').addClass('button-deep-color');
    });

    $('#uploadAvatarCropSubmit').addClass('button-deep-color').mouseover(function(){
        $(this).removeClass('button-deep-color').addClass('button-light-color');
    }).mouseout(function(){
        $(this).removeClass('button-light-color').addClass('button-deep-color');
    });
});