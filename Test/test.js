
// 1) შექმენით ფუნქცია Sum, რომელიც არგუმენტად მიიღებს ორ რიცხვს და დააბრუნებს მათ ჯამს. ფუნქციას გაუწერეთ Default არგუმენტები. პასუხი დააბრუნეთ return-ით.

function Sum(num1=1, num2=1){
    return num1 + num2 
}

console.log(Sum(2, 7))

// 2) შექმენით ფუნქცია Substract, რომელიც არგუმენტად მიიღებს ორ რიცხვს და დააბრუნებს მათ სხვაობას. ფუნქციას გაუწერეთ Default არგუმენტები. პასუხი დააბრუნეთ return-ით.

function Substract(num2=2, num3=1){
    return num2 - num3 
}
console.log(Substract(2, 7))



// 3) შექმენით ფუნქცია Multiply, რომელიც არგუმენტად მიიღებს ორ რიცხვს და დააბრუნებს მათ ნამრავლს. ფუნქციას გაუწერეთ Default არგუმენტები. პასუხი დააბრუნეთ return-ით.

function Multiply(num4=4, num5=2){
    return num4 * num5 
}
console.log(Multiply(9, 9))



// 4) შექმენით ფუნქცია Divide, რომელიც არგუმენტად მიიღებს ორ რიცხვს და დააბრუნებს მათ განაყოფს. ფუნქციას გაუწერეთ Default არგუმენტები. პასუხი დააბრუნეთ return-ით.

function Divide(num6=2, num7=2){
    return num6 / num7 
}
console.log(Divide(100, 10))

// 5) შექმენით ფუნქცია, რომელიც მიიღებს ერთ რიცხვს და შეამოწმებს, არის თუ არა ის კენტი თუ ლუწი,შედეგი დაბეჭდეთ ეკრანზე

function evenOrOdd(num=1){
    if(num % 2 === 0){
        return "Even"
    }else{
        return "Odd"
    }
}

console.log(evenOrOdd(10))




for(let i = 0; i <= 15; i++){
    console.log(i)
}

count = 0

while(count <=15){
    console.log(count)
    count += 1
}


counter = 10

do{
    console.log("მიყვას ყიყლიყო")
    counter--
}while (counter > 0)


function greet(name){
    return `Hello ${name}`
}
console.log(greet('Gvanca'))


const Greet = (name) =>{
    return `Hello ${name}`
}

console.log(greet("Gvanca"))



let personal = {
    'name': 'Gvanca',
    'surname': "Mazanishvili"
}

console.log(personal.name)

