<template>
<div>
    <h1>Shopping Cart</h1>
    <ul>
        <li v-for="product in products" :key="product.id">
            {{product.title}}-- $ {{product.price}}-{{product.quantity}}
        </li>
    </ul>
   <strong> <p class="total">Total: $ {{total}}</p> </strong>

   <button @click="checkout">Checkout</button>
   <p v-if="checkoutStatus">{{checkoutStatus}}</p>
    </div>
</template>

<script>
import {mapState, mapGetters, mapActions} from 'vuex'
export default {
    computed: {
        ...mapGetters('cart', {
            products: 'cartProducts',
            total: 'cartTotal',
        }),
        ...mapState('cart', {
           checkoutStatus: state => state.checkoutStatus,
        }),
    },
    methods: {
      ...mapActions('cart', ['checkout'])
    }
}
</script>

<style lang="css" scoped>
.total{
    color: brown;
}
</style>
