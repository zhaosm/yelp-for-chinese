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
        <v-text-field
          solo-inverted
          flat
          hide-details
          v-model="keywordsEntered"
          label="Search">
        </v-text-field>
        <v-btn
          text
          icon
          @click="getTotalItems()"
        >
          <v-icon>mdi-magnify</v-icon>
        </v-btn>
      </v-row>
    </v-app-bar>
    <v-card cols="12" class="mt-1 mx-auto">
      <v-card-text class="pb-0">
        <div class="d-flex justify-space-between mr-3">
          <div>
            <div class="title" style="color: grey">
              Category
            </div>
            <v-divider class="mt-3"></v-divider>
            <v-row>
              <v-checkbox
                v-for="category in categories"
                :key="category"
                :label="category"
                color="red"
                :value="category"
                class="mt-2 ml-5"
                hide-details
                dense
                v-model="categoriesSelected"
              ></v-checkbox>
            </v-row>
          </div>

          <div>
            <div class="title" style="color: grey">
              Price
            </div>
            <v-divider class="mt-3"></v-divider>
            <v-row>
              <v-checkbox
                v-for="price in prices"
                :key="price"
                :label="`$`.repeat(price)"
                color="red"
                :value="price"
                class="mt-2 ml-5"
                hide-details
                dense
                v-model="pricesSelected"
              ></v-checkbox>
            </v-row>
          </div>

          <div>
            <div class="title" style="color: grey">
              Rating
            </div>
            <v-divider class="mt-3"></v-divider>
            <v-row>
              <v-checkbox
                v-for="rating in ratings"
                :key="rating"
                :label="rating"
                color="red"
                :value="rating"
                class="mt-2 ml-5"
                hide-details
                dense
                v-model="ratingsSelected"
              ></v-checkbox>
            </v-row>
          </div>
        </div>
      </v-card-text>

      <v-card-actions class="justify-end">
        <v-btn
          text
          color="red"
          @click="getTotalItems(); "
        >
          filter
        </v-btn>
      </v-card-actions>

      <v-progress-linear
        :active="loading"
        :indeterminate="loading"
        absolute
        bottom
        color="red"
      ></v-progress-linear>
    </v-card>

    <div v-if="!loading">
      <v-row no-gutters>
        <v-col
          v-for="(item, i) in items"
          :key="i"
          cols="12"
          class="mt-1"
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
                      color="red"
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
                  {{ item.popularReviews[0] }}
                </v-card-text>
              </div>
            </div>
          </v-card>
        </v-col>
      </v-row>

      <!--pagination-->
      <div class="text-center">
        <v-container>
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
        </v-container>
      </div>
    </div>

    <!--scroll to top-->
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
  </div>
</template>

<script>
  import axios from "axios";
  export default {
    data: () => ({
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
      loading: true,
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
