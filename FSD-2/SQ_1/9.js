class A{
    #field = 10
    set field(val){
        this.#field = val;
    }
    get field(){
        return this.#field;
    }
}

let a = new A();
a.field = 20;
console.log(a.field);
