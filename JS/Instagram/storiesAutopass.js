function startAutoPass(delay){
	document.querySelector('.coreSpriteRightChevron').parentElement.click()
	setTimeout(()=>{startAutoPass(delay)},delay)
}
startAutoPass(2000)