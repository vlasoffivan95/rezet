$( document ).ready(function() {
    price = parseInt($('#allprice').val());
    if(price < 300){
    	var value = $('.more_delivery').val();
    	var value_default = $('.default_delivery').val();
    	$('option[value="' + value + '"]').remove();
    	$('option[value="' + value_default + '"]').attr('selected', 'selected');
    }else{
    	$('.hidden_select').css('display', 'block');
    	var value = $('.more_delivery').val();
    	$('option[value="' + value + '"]').attr('selected', 'selected');
    }
});

$('select[name="shipping_options"]').on('change', function(event){
	var value = event.target.value;
	var nowprice = $('#allprice').val();
	var deliveryprice = $('.delivery__' + value).val();
	var newprice = parseFloat(nowprice) + parseFloat(deliveryprice);
	$('.allprice').html(newprice);
})

function addToCart(id){
	$.get('/add-to-cart/', { id:id }).done(function(data){
		var count = parseInt($('.cart_count').html());
		$('.cart_count').html(count + 1);
	});
}

function deleteItemCart(id, element){

	$.get('/delete-cart/', {id:id}).done(function(){
		$(element).parent().parent()[0].remove();
		var price = $(element).context.nextSibling.parentElement.lastElementChild.lastElementChild.firstElementChild.innerText;
		var total_price = $('.total__allprice')
		var newprice = total_price.html() - parseInt(price)
		total_price.html(parseInt(newprice));
		if(newprice == 0){
			$('.total_button').addClass('total_button_disabled');
		}
	})
	
}

function editCount(id, type, price_product, element){
	var newelement = $(element).siblings('.cart_count')
	var count = parseInt(newelement.val())
	var price = $(element).context.offsetParent.lastElementChild.lastElementChild.firstElementChild
	var total_price = $('.total__allprice')
	var delete_button = $(element).parent().parent().prev()[0]
	if(type === 'minus'){
		var newcount = count - 1
		$.get('/edit-count-cart/', {id, type}).done(function(){
			newelement.val(newcount);
			price.innerText = parseInt(price_product) * newcount;
			total_price.html(parseInt(total_price.html()) - parseInt(price_product));
		})
		if(newcount === 0){
			$(element).attr('disabled', 'disabled');
			deleteItemCart(id, delete_button);
		}
	}else{
		var newcount = count + 1
		$.get('/edit-count-cart/', {id, type}).done(function(){
			newelement.val(newcount);
			price.innerText = parseInt(price_product) * newcount;
			total_price.html(parseInt(total_price.html()) + parseInt(price_product));
		})
		if(newcount === 50){
			$(element).attr('disabled', 'disabled');
		}
	}
}

function validateForm(){
	var name = $('[name="name"]');
	var address = $('[name="address"]');
	var phone = $('[name="phone"]');
	var email = $('[name="email"]');

	var name_check = false;
	var address_check = false;
	var phone_check = false;
	var email_check = false;

	if(name.val().length > 2){
		name_check = true;
		name.removeClass('input_error');
		$('.name_error').css('display', 'none');
	}else{
		name_check = false;
		name.addClass('input_error');
		$('.name_error').css('display', 'block');
	}

	if(address.val().length > 3){
		address_check = true;
		address.removeClass('input_error');
		$('.address_error').css('display', 'none');
	}else{
		address_check = false;
		address.addClass('input_error');
		$('.address_error').css('display', 'block');
	}

	if(phone.val().length > 0){
		if(phone.val().length >= 10){
			var re = /^\d[\d\(\)\ -]{4,14}\d$/;
			var valid = re.test(phone.val())
			if(valid){
				phone_check = true;
				phone.removeClass('input_error');
				$('.phone_error').css('display', 'none');
			}else{
				false;
				phone.addClass('input_error');
				$('.phone_error').css('display', 'block');
			}
		}else{
			phone_check = false;
			phone.addClass('input_error');
			$('.phone_error').css('display', 'block');
		}
	}else{
		phone_check = true;
		phone.removeClass('input_error');
		$('.phone_error').css('display', 'none');
	}

	if(email.val().length > 0){
		var re = /^[\w-\.]+@[\w-]+\.[a-z]{2,4}$/i;
		var valid = re.test(email.val())
		if(valid){
			email_check = true;
			email.removeClass('input_error');
			$('.email_error').css('display', 'none');
		}else{
			email_check = false;
			email.addClass('input_error');
			$('.email_error').css('display', 'block');
		}
	}else{
		email_check = true;
		email.removeClass('input_error');
		$('.email_error').css('display', 'none');
	}

	if(name_check && address_check && phone_check && email_check){
		$('.submit_button').removeClass('submit_button_disabled');
		$('.submit_button').removeAttr('disabled');
	}else{
		console.log('this')
		$('.submit_button').addClass('submit_button_disabled');
		$('.submit_button').attr('disabled', 'disabled');
	}

}

$('[name="name"]').on('keyup', function(){
	validateForm();
});

$('[name="address"]').on('keyup', function(){
	validateForm();
});

$('[name="phone"]').on('keyup', function(){
	validateForm();
});

$('[name="email"]').on('keyup', function(){
	validateForm();
});



















