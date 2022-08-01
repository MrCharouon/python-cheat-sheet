def print_arguments():
    ## Print Defined Arguments:
    print("")

    print("Checking required arguments:")
    if args.filt:
        print("Filtered folder : {}".format(args.filt) )
    print("Checking optional arguments:")
    if args.dist:
        print("Computing distances : {}".format(args.dist) )
    if args.div:
        print("Computing diversity and FST : {}".format(args.div) )
    if args.divNS:
        print("Computing N and S diversities : {}".format(args.divNS) )
    if args.matched:
        print("Matching positions (present in 90% of the samples) : {}".format(args.matched) )
    if args.n_threads:
        print("Number of parallel processes : {}".format(args.n_threads) )
    print("")
print_arguments()