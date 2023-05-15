function fsd(subName, cName){
    this.name = subName
    this.cnam = cName
}
    
    fsd.prototype.chName = function nfs(){
    return this.cnam;
    }
    
    let c1 = new fsd("FSD1", "CSE")
    console.log(c1)
    console.log(c1.chName())