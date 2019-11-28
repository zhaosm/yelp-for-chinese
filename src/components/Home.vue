<template>
  <div>
    <v-row no-gutters>
  <v-app-bar
      color="amber"
    >
    <span class="title mx-3">Yelp</span>
    <v-switch
      class="mt-6"
      v-model="forChinese"
      color="red"
    ></v-switch>
    <span v-bind:class="[{ 'grey--text': !forChinese }, 'title ml-0 mr-3']">For Chinese</span>
    <v-text-field
      solo-inverted
      flat
      hide-details
      label="Search"
    />
    <v-btn text icon>
      <v-icon>mdi-magnify</v-icon>
    </v-btn>
  </v-app-bar>
    </v-row>
  <!--<v-row no-gutters>-->
    <!--<v-col class="text-center" cols="3">-->
      <!--<div class="my-1">-->
        <!--<v-btn block>Burgers</v-btn>-->
      <!--</div>-->
    <!--</v-col>-->
    <!--<v-col class="text-center" cols="3">-->
      <!--<div class="my-1">-->
        <!--<v-btn block>Italian</v-btn>-->
      <!--</div>-->
    <!--</v-col>-->
    <!--<v-col class="text-center" cols="3">-->
      <!--<div class="my-1">-->
        <!--<v-btn block>Chinese</v-btn>-->
      <!--</div>-->
    <!--</v-col>-->
    <!--<v-col class="text-center" cols="3">-->
      <!--<div class="my-1">-->
        <!--<v-btn block>Mexican</v-btn>-->
      <!--</div>-->
    <!--</v-col>-->
  <!--</v-row>-->


    <v-row no-gutters>
      <v-col
        v-for="(item, i) in items"
        :key="i"
        cols="12"
        class="my-1"
      >
        <v-card>
          <div class="d-flex flex-no-wrap justify-space-between">
            <!--avatar-->
            <div class="mx-4 my-auto">
            <v-avatar
              style="border-radius: 3%;"
              size="250"
              tile
            >
              <v-img :src="item.img"></v-img>
            </v-avatar>
            </div>

            <!--basic information-->
            <v-col cols="3" class="px-0">
              <v-card-title
                class="headline px-0"
                v-text="item.rank + '. ' + item.name"
              ></v-card-title>
              <v-card-text class="px-0">
                <v-row
                  align="center"
                  class="mx-0"
                >
                  <v-rating
                    :value="item.rating"
                    color="amber"
                    dense
                    half-increments
                    readonly
                    size="14"
                  ></v-rating>

                  <div class="grey--text ml-4">{{ item.rating }} ({{ item.numReviews }} reviews)</div>
                </v-row>

                <div class="subtitle-1 my-3">
                  <span v-for="n in item.cost" :key="n" class="black--text">$</span> <span class="grey--text">• {{ item.type }}</span>
                </div>
                <div class="subtitle-1 black--text my-1">
                  {{ item.phone }}
                </div>
                <div class="subtitle-1 black--text my-1">
                  {{ item.address }}
                </div>
                <div class="subtitle-1 black--text my-1">
                  {{ item.neighborhood }}
                </div>
              </v-card-text>
            </v-col>

            <!--popular review-->
            <div>
              <v-card-text class="pl-0">
                {{ item.popularReview }}
              </v-card-text>
            </div>
          </div>
        </v-card>
      </v-col>
    </v-row>
    <v-btn
            v-scroll="onScroll"
            v-show="fab"
            fab
            dark
            fixed
            bottom
            right
            color="red"
            @click="toTop"
          >
            <v-icon>mdi-chevron-up</v-icon>
          </v-btn>
    <div class="text-center">
    <v-container>
      <v-row justify="center">
        <v-col cols="6">
          <v-container class="max-width">
            <v-pagination
              v-model="page"
              class="my-4"
              :length="pageLength"
            ></v-pagination>
          </v-container>
        </v-col>
      </v-row>
    </v-container>
  </div>

  </div>

</template>

<script>
  export default {
    data: () => ({
      totalItems: Array(100).fill({
          img: 'https://s3-media0.fl.yelpcdn.com/bphoto/hd7Ith2Gm3QnrQqOzI_JvA/ls.jpg',
          rank: 1,
          rating: 4.5,
          numReviews: 3019,
          cost: 2,
          name: 'Poor Calvin\'s',
          type: 'Asian Fusion, Southern, Comfort Food',
          phone: '(404) 254-4051',
          address: '510 Piedmont Ave NE',
          neighborhood: 'Downtown',
          popularReview: '“Amazing place! Took an off from work just to experience this place! It was so worth it! Amazing food. Tried \'The Beast\' sandwich and the \'shawrma platter\'.…”'
        }).concat(Array(100).fill({
          img: 'https://s3-media0.fl.yelpcdn.com/bphoto/_x61pM4WZiji4d2jq1GnYw/ls.jpg',
          rank: 2,
          rating: 5.0,
          numReviews: 1433,
          cost: 2,
          name: 'Aviva by Kameel',
          type: 'Mediterranean, Juice Bars & Smoothies, Middle Eastern',
          phone: '(404) 698-3600',
          address: '225 Peachtree St NE',
          neighborhood: 'Downtown',
          popularReview: '“Hubby and I were in town for the weekend from CA and wanted to try some yummy fried chicken so took to Yelp to search. Came across Gus\'s and was super happy…”'
        })),
      page: 1,
      pageLength: 20,
      fab: false,
      forChinese: true,
    }),

    computed: {
      items: function() {
        return this.totalItems.slice((this.page - 1) * 10, this.page * 10 + 1);
      }
    },

    watch: {
      page: function(value) {
        console.log('page ' + value);
        this.toTop();
      },

      forChinese: function(value) {
        console.log('for chinses' + value);
      }
    },

    methods: {
      onScroll (e) {
        if (typeof window === 'undefined') return;
        const top = window.pageYOffset || e.target.scrollTop || 0;
        this.fab = top > 20;
      },
      toTop () {
        console.log('toTop');
        window.scrollTo({ top: 0, left: 0, behavior: 'smooth'});
      }
    },

    mounted: function() {
      window.scrollTo({ top: 0, left: 0});
    }
  }
</script>