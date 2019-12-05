<template>
  <div>
    <v-app-bar
      color="amber"
    >
      <v-row align="center">
        <span class="title ma-3">Yelp</span>
        <v-switch
          hide-details
          v-model="forChinese"
          color="red"
        ></v-switch>
        <span v-bind:class="[{ 'grey--text': !forChinese }, 'title ml-0 mr-3']">For Chinese</span>
      </v-row>
    </v-app-bar>
    <v-row>
        <v-col v-for="(item,i) in pic" cols = "2"
                    :key="i"
                    >
          <v-img :src="item.src"
          ></v-img>
        </v-col>
    </v-row>
    <v-container fluid>
        <v-row>
        <v-col   cols = "6" >
            <v-card
                :loading="loading"
                >
                <v-card-title>Cafe Badilico</v-card-title>
                <v-card-text>
                    <v-row
                    align="center"
                    class="mx-0"
                    >
                        <v-rating
                            :value="4.5"
                            color="amber"
                            size = "20"
                            dense
                            half-increments
                            readonly
                        ></v-rating>
                
                        <div class="grey--text ml-4">4.5 (413)</div>
                    </v-row>
                    <div class="my-4 subtitle-1 black--text">
                    $ • Italian, Cafe
                    </div>
                    <div>Small plates, salads & sandwiches an inteimate setting with 12 indoor seats plus patio seating.</div>
                </v-card-text>
                    
            </v-card>
            <v-divider></v-divider>
            <v-spacer></v-spacer>
        
            <v-row> 
                <v-col cols = "6.5">
                    <v-card
                    :loading="loading"
                    >
                        <v-card-title><p class="font-weight-medium">DETAIL </p></v-card-title>
                        <v-row v-for = "i in 5" :key = "i"
                        align="center"
                        class="mx-0"
                        >
                            <v-rating 
                                :value="6-i"
                                color="amber"
                                size = "30"
                                dense
                                half-increments
                                readonly
                            ></v-rating>
                    
                            <div>
                                <v-chip
                                    class="ma-2"
                                    color="green"
                                    text-color="white"
                                >
                                    <v-avatar
                                    left
                                    class="green darken-4"
                                    >
                                    {{nums[i-1]}}
                                    </v-avatar>
                                    {{good[i-1]}}
                                </v-chip>
                            </div>
                        </v-row>
                    </v-card>
                </v-col>
                <v-col cols = "5.5">
                    <v-card
                    :loading="loading"
                    >
                        <v-card-title><p class="font-weight-medium">DISHES </p>
                        </v-card-title>
                        <div>
                        <v-chip v-for = "i in 7" :key = "i"
                            class="ma-2"
                            color="cyan"
                            label
                            text-color="white"
                        >
                            <v-icon left>mdi-label</v-icon>
                            {{dishes[i-1]}}
                        </v-chip>
                        </div>
                    </v-card>
                </v-col>
            </v-row>

       
        </v-col>
       
        <v-col cols = "12" sm = "6">
            <v-carousel>
                <v-carousel-item
                    v-for="(item,i) in items"
                    :key="i"
                    :src="item.src"
                    reverse-transition="fade-transition"
                    transition="fade-transition"
                >
                    </v-carousel-item>
            </v-carousel>
        </v-col>
    </v-row>

    <v-subheader inset >
              <p class = "display-2">Recommended Reviews</p>
    </v-subheader>
    <v-divider></v-divider>
    <v-col cols = "12" sm = "11.5" offset = "0.5">
        <v-row v-for = "i in 10" :key = "i">
            <v-card 
                class="mx-auto"
                color="#26c6da"
                dark
            >
                <v-card-title>
                    <v-icon
                    large
                    left
                    >
                    mdi-twitter
                    </v-icon>
                    <span class="title font-weight-light">Great</span>
                </v-card-title>
            
                <v-card-text class="headline font-weight-bold">
                    "“Hubby and I were in town for the weekend from CA and wanted to try some yummy fried chicken so took to Yelp to search. Came across Gus's and was super happy…”"
                </v-card-text>
            
                <v-card-actions>
                    <v-list-item class="grow">
                    <v-list-item-avatar color="grey darken-3">
                        <v-img
                        class="elevation-6"
                        src="https://avataaars.io/?avatarStyle=Transparent&topType=ShortHairShortCurly&accessoriesType=Prescription02&hairColor=Black&facialHairType=Blank&clotheType=Hoodie&clotheColor=White&eyeType=Default&eyebrowType=DefaultNatural&mouthType=Default&skinColor=Light"
                        ></v-img>
                    </v-list-item-avatar>
            
                    <v-list-item-content>
                        <v-list-item-title>Evan You</v-list-item-title>
                    </v-list-item-content>
                    <v-rating
                        :value="4.5"
                        color="amber"
                        large
                        dense
                        half-increments
                        readonly
                        size="14"
                    ></v-rating>
                    <v-row
                        align="center"
                        justify="end"
                    >
                        <v-icon class="mr-1">mdi-heart</v-icon>
                        <span class="subheading mr-2">256</span>
                        <span class="mr-1">·</span>
                        <v-icon class="mr-1">mdi-share-variant</v-icon>
                        <span class="subheading">45</span>
                    </v-row>
                    </v-list-item>
                </v-card-actions>
            </v-card>
            <v-divider inset ></v-divider>
            <v-spacer ></v-spacer>
        </v-row>
    </v-col>
    <div class="text-center">
        <v-row justify="center">
        <v-col cols="6">
            <v-container class="max-width">
            <v-pagination
                v-model="page"
                class="my-4"
                :length="pageLength"
                color="red"
            ></v-pagination>
            </v-container>
        </v-col>
          </v-row>
      </div>

    </v-container>
    
  </div>
</template>

<script>
  import axios from "axios";
  export default {
    data: () => ({
        good:["Excellent","Good","Average","Fair","Poor",],
        dishes:[ "Hotpot","Sichuan Pork","Braised Pork Balls in Gravy","Shrimp with Vermicelli and Garlic","Dumplings","Chow Mein","Peking Roasted Duck",],
        nums:[11,8,9,3,1],
        pic:[
            {
            src: 'https://i.ibb.co/fFCgyNg/position5.jpg',
            },
            {
            src: 'https://i.ibb.co/74hJ1Bw/position4.jpg',
            },
            {
            src: 'https://i.ibb.co/MpRHjzw/position3.jpg',
            },
            {
            src: 'https://i.ibb.co/RTnMz4Y/position2.jpg',
            },
            {
            src: 'https://i.ibb.co/VYnfJT6/position1.jpg',
            },
            {
            src: 'https://i.ibb.co/R7W1Ym6/food1.jpg',
            },

        ],
        items: [
            {
            src: 'https://i.ibb.co/87fmWTY/food6.jpg',
            },
            {
            src: 'https://i.ibb.co/Fh0tLgC/food4.jpg',
            },
            {
            src: 'https://i.ibb.co/VCcd7GS/food3.jpg',
            },
            {
            src: 'https://i.ibb.co/27nr2ft/food2.jpg',
            },
            {
            src: 'https://i.ibb.co/R7W1Ym6/food1.jpg',
            },
            
        ],
        loading: false,
        selection: 1,
      totalItems: [],
      page: 1,
      fab: false,
      forChinese: true,
      categories: ['Burgers', 'Italian', 'Chinese', 'Mexican'],
      prices: [1, 2, 3, 4],
      ratings: ['0-1', '1-2', '2-3', '3-4', '4-5'],
      categoriesSelected: [],
      pricesSelected: [],
      ratingsSelected: [],
      keywordsEntered: "",
    }),

    computed: {
      items: function() {
        return this.totalItems.slice((this.page - 1) * 10, this.page * 10 + 1);
      },
      pageLength: function() {
        return Math.ceil(this.totalItems.length / 10);
      }
    },

    watch: {
      page: function(value) {
        this.page = value;
        this.toTop();
      },
      forChinese: function() {
        this.getTotalItems();
      },
    },

    methods: {
      onScroll (e) {
        if (typeof window === 'undefined') return;
        const top = window.pageYOffset || e.target.scrollTop || 0;
        this.fab = top > 20;
      },
      toTop () {
        window.scrollTo({ top: 0, left: 0, behavior: 'smooth'});
      },
      getTotalItems() {
        this.loading = true;
        const path = "http://localhost:5000/totalItems";
        const params = {
          forChinese: this.forChinese,
          keywords: this.keywordsEntered,
          filter: { category: this.categoriesSelected, price: this.pricesSelected, rating: this.ratingsSelected }};
        axios
          .get(path, { params })
          .then(res => {
            this.totalItems = res.data;
            this.loading = false;
          })
          .catch(error => {
            console.error(error);
          });
      }
    },

    mounted: function() {
      window.scrollTo({ top: 0, left: 0});
    },

    created: function() {
      this.getTotalItems();
    }
  }
</script>
