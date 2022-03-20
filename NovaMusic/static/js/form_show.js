function ShowReplyForm(comment_id){
	const form = document.getElementById(`collapseExample${comment_id}`)
	if (form.style.display === 'none'){
		form.style.display = 'block'
	} else {
		form.style.display = 'none'
	}
}